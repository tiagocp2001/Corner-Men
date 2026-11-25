# Troca a cabeça base pela cabeça de outro atleta em cada fotograma de uma animação da PixelLab, sem gerações.
# Funciona porque as 40 cabeças foram feitas sobre o mesmo corpo f (o corpo é igual do peito para baixo).
# 1) encontra onde está a cabeça base no fotograma (deslocação e um pequeno ângulo);
# 2) apaga-a (mantendo as luvas que estejam à frente da cara); 3) põe lá a cabeça do atleta com a mesma deslocação/ângulo.
import sys, os, math
import numpy as np
from PIL import Image
AQUI = os.path.dirname(os.path.abspath(__file__))
CAB = os.path.join(AQUI, '..', '..', 'cabecas-pixellab', 'variantes')
DIRS = ['south', 'south-east', 'east', 'north-east', 'north', 'north-west', 'west', 'south-west']
S = dict(zip(DIRS, [28, 26, 24, 25, 27, 26, 25, 26]))       # linha dos ombros em cada vista (verificar.py)
def img(p): return np.array(Image.open(p).convert('RGBA')).astype(int)
def luva(a): return (a[..., 3] > 0) & (a[..., 0] > 130) & (a[..., 0] > 2 * a[..., 1])
def cabeca(vista, n):
    """cabeça (e pescoço) do atleta n nesta vista: tudo acima da linha dos ombros que não seja luva"""
    a = img(os.path.join(CAB, '00-corpo-base' if n == 0 else f'{n:02d}', vista + '.png'))
    m = (a[..., 3] > 0) & ~luva(a); m[S[vista]:, :] = False
    return a, m
def scale2x(a):
    """Scale2x (EPX): aumenta 2x a pixel art sem desfocar"""
    h, w = a.shape[:2]; p = np.pad(a, ((1, 1), (1, 1), (0, 0)), mode='edge'); out = np.zeros((h * 2, w * 2, a.shape[2]), a.dtype)
    B, D, E, F, H = p[:-2, 1:-1], p[1:-1, :-2], p[1:-1, 1:-1], p[1:-1, 2:], p[2:, 1:-1]
    eq = lambda x, y: (x == y).all(-1)
    c = ~eq(B, H) & ~eq(D, F)
    out[0::2, 0::2] = np.where((c & eq(D, B))[..., None], D, E); out[0::2, 1::2] = np.where((c & eq(B, F))[..., None], F, E)
    out[1::2, 0::2] = np.where((c & eq(D, H))[..., None], D, E); out[1::2, 1::2] = np.where((c & eq(H, F))[..., None], F, E)
    return out
def roda(a, m, ang):
    """RotSprite: aumenta 8x com Scale2x, roda, e volta ao tamanho pegando na cor mais comum de cada bloco"""
    if not ang: return a, m
    h, w = m.shape; b = a.copy(); b[~m] = 0
    for _ in range(3): b = scale2x(b)
    H, W = b.shape[:2]; cy, cx = S_v * 8, W / 2
    c, s = math.cos(math.radians(ang)), math.sin(math.radians(ang))
    yy, xx = np.mgrid[0:H, 0:W]; X = c * (xx - cx) + s * (yy - cy) + cx; Y = -s * (xx - cx) + c * (yy - cy) + cy
    Xi, Yi = np.round(X).astype(int), np.round(Y).astype(int); ok = (Xi >= 0) & (Xi < W) & (Yi >= 0) & (Yi < H)
    r = np.zeros_like(b); r[ok] = b[Yi[ok], Xi[ok]]
    out = np.zeros_like(a); om = np.zeros_like(m)
    for y in range(h):
        for x in range(w):
            blk = r[y * 8 + 2:y * 8 + 6, x * 8 + 2:x * 8 + 6].reshape(-1, 4)       # centro do bloco: mais nítido
            blk = [tuple(p) for p in blk if p[3] > 0]
            if len(blk) >= 8:
                from collections import Counter
                out[y, x] = Counter(blk).most_common(1)[0][0]; om[y, x] = True
    return out, om
def acha(fr, ab, mb):
    """onde está a cabeça base neste fotograma: melhor (dx, dy, ângulo)"""
    best = None; H, W = fr.shape[:2]; ys, xs = np.nonzero(mb)
    for ang in (0, -8, 8, -16, 16, -24, 24):
        a2, m2 = roda(ab, mb, ang); ys, xs = np.nonzero(m2)
        for dy in range(-2, H - 60 + 3):
            for dx in range(0, W - 40):
                Y, X = ys + dy, xs + dx
                ok = (Y >= 0) & (Y < H) & (X < W)
                if ok.sum() < len(ys) * 0.9: continue
                d = np.abs(fr[Y[ok], X[ok], :3] - a2[ys[ok], xs[ok], :3]).sum(1)
                sc = (d < 40).mean()
                if best is None or sc > best[0]: best = (sc, dx, dy, ang)
    return best
def mapa_pele(vista, n):
    """cores da pele: o corpo é o mesmo, por isso cada píxel do corpo base tem o par certo no corpo do atleta"""
    a = img(os.path.join(CAB, '00-corpo-base', vista + '.png')); b = img(os.path.join(CAB, f'{n:02d}', vista + '.png'))
    from collections import Counter, defaultdict
    par = defaultdict(Counter)
    for y in range(S[vista] + 3, 60):
        for x in range(40):
            if a[y, x, 3] and b[y, x, 3] and not luva(a[y:y + 1, x:x + 1])[0, 0]:
                ca, cb = tuple(a[y, x, :3]), tuple(b[y, x, :3])
                if ca != cb: par[ca][cb] += 1
    return {k: v.most_common(1)[0][0] for k, v in par.items()}
def pinta(fr, mapa):
    """troca cada cor de pele do fotograma pela cor do atleta (a mais parecida do mapa)"""
    out = fr.copy(); ks = np.array(list(mapa.keys())); vs = np.array(list(mapa.values()))
    if not len(ks): return out
    m = fr[..., 3] > 0; ys, xs = np.nonzero(m)
    c = fr[ys, xs, :3]; d = np.abs(c[:, None, :] - ks[None, :, :]).sum(2); j = d.argmin(1); ok = d[np.arange(len(j)), j] < 30
    out[ys[ok], xs[ok], :3] = vs[j[ok]]
    return out
def acha_contorno(fr, ab, mb):
    """quando a cabeça está muito inclinada, compara só a forma (contorno), não as cores"""
    H, W = fr.shape[:2]; alpha = fr[..., 3] > 0; best = None
    for ang in range(-32, 33, 4):
        a2, m2 = roda(ab, mb, ang); ys, xs = np.nonzero(m2)
        for dy in range(-4, H - 60 + 4):
            for dx in range(0, W - 40):
                Y, X = ys + dy, xs + dx; ok = (Y >= 0) & (Y < H) & (X >= 0) & (X < W)
                if ok.sum() < len(ys) * 0.9: continue
                dentro = alpha[Y[ok], X[ok]].mean()                         # a cabeça tapa o desenho
                reg = alpha[max(0, dy):S_v + dy, max(0, dx):dx + 40]; fora = reg.sum() - alpha[Y[ok], X[ok]].sum()
                sc = dentro - 0.5 * fora / max(1, len(ys))                  # e não sobra desenho à volta
                if best is None or sc > best[0]: best = (sc, dx, dy, ang)
    return best
def troca(fr, vista, n, palpite=None):
    fr = pinta(fr, mapa_pele(vista, n))
    ab, mb = cabeca(vista, 0); an, mn = cabeca(vista, n)
    global S_v; S_v = S[vista]
    sc, dx, dy, ang = acha(fr, ab, mb)
    if sc < 0.8: _, dx, dy, ang = acha_contorno(fr, ab, mb)          # cabeça muito inclinada: pela forma
    out = fr.copy(); H, W = fr.shape[:2]
    a2, m2 = roda(ab, mb, ang)                          # apaga a cabeça base (com folga), menos as luvas
    if ang: m2 = m2 | roda(ab, mb, ang // 2)[1] | mb     # inclinada: apaga também por onde ela passou (restos da cara antiga)
    ys, xs = np.nonzero(m2)
    for y, x in zip(ys, xs):
        for dy2 in (-2, -1, 0, 1, 2):
            for dx2 in (-2, -1, 0, 1, 2):
                Y, X = y + dy + dy2, x + dx + dx2
                if 0 <= Y < H and 0 <= X < W and Y < S_v + dy and not luva(fr[Y:Y + 1, X:X + 1])[0, 0]: out[Y, X] = 0
    an2, mn2 = roda(an, mn, ang)                        # põe a cabeça nova
    ys, xs = np.nonzero(mn2)
    for y, x in zip(ys, xs):
        Y, X = y + dy, x + dx
        if 0 <= Y < H and 0 <= X < W and not luva(fr[Y:Y + 1, X:X + 1])[0, 0]: out[Y, X] = an2[y, x]
    from scipy import ndimage                            # limpa restos soltos (1-3 píxeis) da cara antiga
    lab, k = ndimage.label(out[..., 3] > 0, structure=np.ones((3, 3)))
    if k > 1:
        tam = ndimage.sum(np.ones_like(lab), lab, range(1, k + 1))
        for i, t in enumerate(tam):
            if t <= 3: out[lab == i + 1] = 0
    return out, sc, ang
if __name__ == '__main__':
    pasta, vista, n, saida = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4]
    os.makedirs(saida, exist_ok=True)
    for i in range(8):
        fr = img(os.path.join(pasta, f'{i}.png'))
        o, sc, ang = troca(fr, vista, n)
        Image.fromarray(o.astype('uint8'), 'RGBA').save(os.path.join(saida, f'{i}.png')); print(i, f'encaixe {sc:.2f}', 'ângulo', ang)
