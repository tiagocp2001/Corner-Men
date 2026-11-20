# Jab (mão da frente, guarda ortodoxa), à cabeça: 6 fotogramas, 8 vistas, feito em código a partir da guarda.
# A luva da frente sai na direção para onde ele está virado; o braço é desenhado do ombro até à luva.
# Nas vistas de frente a luva vem para nós (cresce); nas de costas vai para longe (encolhe).
# Uso: python3 jab.py <pasta-com-as-8-vistas> [...]  -> jab.gif
import sys, os, math
from PIL import Image, ImageDraw, ImageFont
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import saltitar as S, guarda as G, andar as A
AQUI = os.path.dirname(os.path.abspath(__file__))
EXT = [0, 0.55, 1.0, 1.0, 0.6, 0.25]          # quanto o braço está esticado em cada fotograma
DUR = [90, 50, 70, 90, 70, 70]
INC = [0, 1, 1, 1, 0, 0]                        # o corpo de cima acompanha o golpe (1 píxel)

def comps(m):
    cs = []; seen = set()
    for p in sorted(m):
        if p in seen: continue
        st = [p]; c = []
        while st:
            q = st.pop()
            if q in seen or q not in m: continue
            seen.add(q); c.append(q); x, y = q; st += [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        cs.append(set(c))
    return sorted(cs, key=len, reverse=True)

def luva_frente(im, t):
    """píxeis da luva da frente (mão esquerda): à frente, na direção para onde está virado; nas vistas
    de frente/costas, a do lado esquerdo dele"""
    fx, fy = A.FRENTE[t]
    lx, ly = fy, -fx                                   # esquerda dele, no ecrã
    sc = lambda c: sum((x*fx + y*fy) * 1.0 + (x*lx) * 0.6 for x, y in c) / len(c)
    cs = [c for c in comps(G.luvas(im)) if len(c) >= 20]
    if len(cs) >= 2: return max(cs[:2], key=sc)
    c = cs[0]
    if len(c) < 100: return c                          # só se vê uma luva
    # duas luvas coladas: corta pela mediana na direção do golpe
    f = (lambda x, y: x*fx + 0.2*y*fy) if fx else (lambda x, y: x*lx)
    pr = sorted(f(x, y) for x, y in c); med = pr[len(pr)//2]
    return {(x, y) for x, y in c if f(x, y) >= med}

def cores(im):
    px = im.load(); w, h = im.size
    pele = Counter(px[x, y][:3] for y in range(18, 40) for x in range(w) if S.cls(px[x, y]) == 's').most_common(3)
    cont = Counter(px[x, y][:3] for y in range(h) for x in range(w) if S.cls(px[x, y]) == '#').most_common(1)[0][0]
    lum = lambda c: .3*c[0] + .59*c[1] + .11*c[2]
    return sorted([c for c, _ in pele], key=lum), cont          # escura, média, clara

PADX = 10                                       # o golpe sai do quadro de 40: trabalha-se num de 60
W2 = 40 + 2*PADX
def larga(im):
    out = Image.new('RGBA', (W2, 60)); out.alpha_composite(im, (PADX, 0)); return out
def desvia(im, K, dx):
    if not dx: return im
    out = Image.new('RGBA', im.size); po, pi = out.load(), im.load()
    for y in range(60):
        for x in range(W2):
            X = x - dx if y <= K else x
            if 0 <= X < W2: po[x, y] = pi[X, y]
    return out
def tapa(im, buraco):
    """onde estava a luva: dentro do corpo copia o vizinho; fora do corpo fica transparente"""
    out = im.copy(); px = out.load()
    for p in buraco: px[p] = (0, 0, 0, 0)
    fora = set()
    for (x, y) in buraco:
        esq = any(px[i, y][3] and (i, y) not in buraco for i in range(0, x))
        dir_ = any(px[i, y][3] and (i, y) not in buraco for i in range(x+1, W2))
        if not (esq and dir_): fora.add((x, y))
    falta = set(buraco) - fora
    while falta:
        feito = set()
        for (x, y) in falta:
            for a, b in ((0, -1), (-1, 0), (1, 0), (0, 1)):
                q = (x+a, y+b)
                if 0 <= q[0] < W2 and 0 <= q[1] < 60 and px[q][3] and q not in falta:
                    px[x, y] = px[q]; feito.add((x, y)); break
        if not feito: break
        falta -= feito
    return out

def braco(dr, a, b, pele, cont, w=6):
    """braço do ombro (a) à luva (b): contorno escuro, pele por dentro e um tom mais escuro por baixo"""
    dr.line([a, b], fill=cont + (255,), width=w)
    dr.line([(a[0], a[1] + 0.5), (b[0], b[1] + 0.5)], fill=pele[0] + (255,), width=w - 2)
    dr.line([(a[0], a[1] - 0.5), (b[0], b[1] - 0.5)], fill=pele[1] + (255,), width=w - 3)
    dr.line([(a[0], a[1] - 1.5), (b[0], b[1] - 1.5)], fill=pele[-1] + (255,), width=1)

def quadro(im, t, base, ext, inc):
    fx, fy = A.FRENTE[t]
    K, _ = S.marks(base)
    lu = {(x + PADX, y) for x, y in luva_frente(base, t)}
    im = larga(im); base = larga(base)
    xs = [x for x, _ in lu]; ys = [y for _, y in lu]
    x0, y0, x1, y1 = min(xs), min(ys), max(xs), max(ys)
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    pele, cont = cores(base)
    luva = Image.new('RGBA', (x1-x0+1, y1-y0+1)); pl = luva.load(); pi = im.load()
    for (x, y) in lu: pl[x-x0, y-y0] = pi[x, y]
    corpo = tapa(im, lu) if ext > 0 else im.copy()
    if inc: corpo = desvia(corpo, K, inc * fx)
    if ext == 0: return corpo
    # para onde vai a luva
    lado = abs(fx) > 0 and fy == 0
    alc = (9 if lado else 8 if fx else 0) * ext
    if fx: dx = fx * alc
    elif fy > 0: dx = (W2/2 - cx) * 0.6 * ext                            # de frente: vem para nós, para o meio
    else: dx = (W2/2 - cx) * 0.3 * ext                                   # de costas: vai para a frente, junto à cabeça
    dy = (fy * 2 if fy > 0 else -4) * ext if not fx else (fy * 2 * ext - (1 if lado else 0) * ext)
    esc = 1 + (0.5 if fy > 0 else -0.2 if fy < 0 else 0) * ext * (1 if not fx else 0.4)
    L = luva.resize((max(1, round(luva.width*esc)), max(1, round(luva.height*esc))), Image.NEAREST)
    nx, ny = cx + dx + inc*fx, cy + dy
    # ombro: atrás da luva da guarda, um pouco acima
    ox, oy = cx - fx*4 + inc*fx, y0 + 2
    dr = ImageDraw.Draw(corpo)
    if True:                                                        # de costas vê-se o braço por cima do ombro
        braco(dr, (ox, oy), (nx - fx*L.width*0.3, ny), pele, cont)
    out = corpo.copy()
    if fy < 0 and not fx:                                           # de costas: a luva passa por trás da cabeça/ombro
        tmp = Image.new('RGBA', out.size); tmp.alpha_composite(L, (round(nx - L.width/2), round(ny - L.height/2)))
        tmp.alpha_composite(corpo); return tmp   # a luva fica atrás do corpo e do braço (está mais longe)
    out.alpha_composite(L, (round(nx - L.width/2), round(ny - L.height/2)))
    return out

def fotogramas(pasta):
    r = {}
    for n, t in S.ORD:
        base = Image.open(os.path.join(S.BASE, n + '.png')).convert('RGBA')
        im = Image.open(os.path.join(pasta, n + '.png')).convert('RGBA')
        r[n] = [quadro(im, t, base, e, i) for e, i in zip(EXT, INC)]
    return r

def gif(pastas, saida):
    f2 = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 18)
    F = [fotogramas(p) for p in pastas]
    Z, PAD, LAB = 4, 4, 28; frames = []
    for i in range(len(EXT)):
        fr = Image.new('RGBA', (W2*8*Z, (60+PAD)*len(pastas)*Z + LAB), (60, 60, 70, 255)); dr = ImageDraw.Draw(fr)
        for k, (n, t) in enumerate(S.ORD):
            dr.text((k*W2*Z+6, (60+PAD)*len(pastas)*Z+4), t, fill=(255, 220, 120), font=f2)
            for r in range(len(pastas)):
                ox, oy = k*W2*Z, r*(60+PAD)*Z
                dr.ellipse((ox+16*Z, oy+57*Z, ox+44*Z, oy+60*Z), fill=(38, 38, 46, 255))
                fr.alpha_composite(F[r][n][i].resize((W2*Z, 60*Z), Image.NEAREST), (ox, oy))
        frames.append(fr.convert('RGB'))
    frames[0].save(saida, save_all=True, append_images=frames[1:], duration=[400] + DUR[1:], loop=0)
    return frames

if __name__ == '__main__':
    fr = gif(sys.argv[1:] or [S.BASE], os.path.join(AQUI, 'jab.gif'))
    fr[3].save(os.path.join(AQUI, 'jab-esticado.png'))
