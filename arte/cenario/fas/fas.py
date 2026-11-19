# Fãs do público, na mesma arte dos atletas: cabeça tirada das cabeças dos atletas (mesma escala, ~32 px/m)
# + tronco sentado com t-shirt desenhado aqui com 3 tons (claro/médio/escuro) e contorno de 1 píxel.
import os, sys, random
from PIL import Image, ImageSequence
from collections import Counter
AQUI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.join(AQUI, '..', '..', '..')
CAB = os.path.join(REPO, 'arte', 'cabecas-pixellab')
GIFS = '/tmp/claude-0/-home-user-Corner-Men/d38ab75d-3fb7-5fe2-9b4c-05387542f032/images/'
OUT = (10, 8, 10)
W, H = 28, 40
def lum(p): return .3*p[0] + .59*p[1] + .11*p[2]
def isred(p): return p[0] > 110 and p[0] > 2.2*p[1] and p[0] > p[2] + 40
def isskin(p): return p[3] and p[0] > 90 and p[0] > p[2] + 25 and p[0] >= p[1] and p[1] > 0.35*p[0] and not isred(p)
def cabeca(im):
    """recorta a cabeça pela forma dela: cabelo, cara e queixo (até à linha do maxilar); pescoço e ombros ficam de fora.
    Devolve a cabeça numa tela de 28 de largura, a rampa de pele e a linha do pescoço (onde assenta a gola)."""
    px = im.load(); w, h = im.size
    # luvas = manchas vermelhas grandes (os lábios, pequenos, ficam na cara)
    red = {(x, y) for y in range(h) for x in range(w) if px[x, y][3] and isred(px[x, y])}
    luva = set(); vis = set()
    for p in red:
        if p in vis: continue
        st = [p]; comp = []
        while st:
            q = st.pop()
            if q in vis or q not in red: continue
            vis.add(q); comp.append(q); st += [(q[0] + a, q[1] + b) for a in (-1, 0, 1) for b in (-1, 0, 1)]
        if len(comp) >= 12: luva |= set(comp)
    ok = lambda x, y: 0 <= x < w and 0 <= y < h and px[x, y][3] and (x, y) not in luva
    dark = lambda x, y: px[x, y][3] and sum(px[x, y][:3]) < 60
    ys = [y for y in range(h) if any(px[x, y][3] for x in range(w))]; top = ys[0]
    xs = [x for y in range(top, top + 6) for x in range(w) if px[x, y][3]]; cx = round(sum(xs) / len(xs))
    def corrida(y):
        x0 = cx
        if not ok(x0, y):
            cand = [x for x in range(w) if ok(x, y)]
            if not cand: return None
            x0 = min(cand, key=lambda x: abs(x - cx))
        l = x0
        while ok(l - 1, y): l -= 1
        r = x0
        while ok(r + 1, y): r += 1
        return l, r
    # pescoço: a linha mais estreita por baixo da cara (antes das luvas)
    cand = []
    for y in range(top + 14, min(h, top + 27)):
        if sum(1 for x in range(w) if (x, y) in luva) >= 3: break
        c = corrida(y)
        if c and c[1] - c[0] >= 2: cand.append((c[1] - c[0], y, c))
    _, rn, (nl, nr) = min(cand)
    lim = {}
    for x in range(w):
        if nl <= x <= nr:                       # no pescoço: a cabeça acaba na linha preta do maxilar
            j = rn
            for y in range(rn, rn - 4, -1):
                if dark(x, y): j = y; break
            lim[x] = j
        else:                                   # ao lado do pescoço: desce enquanto houver cara, sem entrar nos ombros
            y = top
            while y < h and not ok(x, y) and y < rn: y += 1
            while y + 1 <= rn + 2 and ok(x, y + 1): y += 1
            lim[x] = min(y, rn + 2)
    out = Image.new('RGBA', (W, rn - top + 4)); po = out.load()
    for x in range(w):
        X = x - cx + W // 2
        if not 0 <= X < W: continue
        for y in range(top, lim[x] + 1):
            if ok(x, y): po[X, y - top] = px[x, y]
    # restos soltos dos ombros ao lado do pescoço (linhas finas fora da cara) saem
    for yy in range(rn - top + 1, out.size[1]):
        for X in range(W):
            if not po[X, yy][3]: continue
            viz = sum(1 for a in (-1, 0, 1) for b in (-1, 0, 1) if (a or b) and 0 <= X + a < W and 0 <= yy + b < out.size[1] and po[X + a, yy + b][3])
            longe = X < nl - cx + W // 2 - 3 or X > nr - cx + W // 2 + 3
            if longe and viz <= 3: po[X, yy] = (0, 0, 0, 0)
    pele = Counter(px[x, y][:3] for y in range(top, rn) for x in range(w) if isskin(px[x, y]))
    tons = sorted([c for c, _ in pele.most_common(6)], key=lum, reverse=True)
    rampa = (tons[0], tons[len(tons)//2], tons[-1]) if tons else ((240, 190, 150), (215, 160, 120), (170, 110, 80))
    return out, rampa, rn - top
def frames_gif(n): return [f.convert('RGBA') for f in ImageSequence.Iterator(Image.open(f'{GIFS}{n}.gif'))]
def fontes():
    """cabeças de frente (vista 1) e de costas (vista 6) das cabeças que já existem"""
    f = []
    base = os.path.join(CAB, 'variantes', '00-corpo-base')
    f.append((Image.open(os.path.join(base, 'south-west.png')).convert('RGBA'), Image.open(os.path.join(base, 'north.png')).convert('RGBA'), Image.open(os.path.join(base, 'south.png')).convert('RGBA'), Image.open(os.path.join(base, 'west.png')).convert('RGBA')))
    v1 = os.path.join(CAB, 'variantes', '01')
    if os.path.exists(os.path.join(v1, 'south-west.png')):
        f.append((Image.open(os.path.join(v1, 'south-west.png')).convert('RGBA'), Image.open(os.path.join(v1, 'north.png')).convert('RGBA'), Image.open(os.path.join(v1, 'south.png')).convert('RGBA'), Image.open(os.path.join(v1, 'west.png')).convert('RGBA')))
    for n in (1, 4, 7):                                       # a, c, b (os GIFs da PixelLab; a das tranças saiu)
        if os.path.exists(f'{GIFS}{n}.gif'):
            fr = frames_gif(n); f.append((fr[7], fr[4], fr[0], fr[6]))
    return f
ROUPA = [((236, 72, 64), (200, 40, 40), (140, 26, 34)), ((92, 140, 230), (50, 96, 196), (30, 56, 130)),
         ((240, 238, 230), (205, 202, 192), (150, 146, 140)), ((90, 90, 100), (60, 60, 70), (36, 36, 44)),
         ((110, 190, 110), (60, 140, 70), (36, 90, 46)), ((250, 214, 90), (220, 170, 40), (160, 110, 24)),
         ((170, 110, 200), (120, 70, 150), (78, 42, 104)), ((250, 160, 90), (214, 110, 50), (150, 70, 30)),
         ((96, 200, 210), (40, 140, 160), (24, 90, 110))]
CALCA = [((80, 100, 150), (52, 70, 116), (34, 46, 80)), ((70, 70, 76), (48, 48, 54), (30, 30, 36)), ((150, 130, 100), (116, 98, 72), (80, 66, 48))]
def corpo(pose, costas, roupa, calca, pele):
    """tronco sentado: mapa de partes -> cor com 3 tons; luz da esquerda; contorno de 1 píxel por fora"""
    m = {}
    def put(x, y, parte):
        if 0 <= x < W and 0 <= y < H: m[(x, y)] = parte
    for y in range(20, 23):                                   # pescoço
        for x in range(12, 16): put(x, y, 'pele')
    for y in range(22, 35):                                   # t-shirt
        x0, x1 = (9, 18) if y == 22 else (8, 19)
        for x in range(x0, x1 + 1): put(x, y, 'roupa')
    for y in range(34, 38):                                   # coxas (sentado, vistas de frente)
        for x in range(7, 21): put(x, y, 'calca')
    if pose == 'sentado':
        for y in range(23, 33):
            for x in (5, 6, 7): put(x, y, 'roupa' if y < 26 else 'pele')
            for x in (20, 21, 22): put(x, y, 'roupa' if y < 26 else 'pele')
        if not costas:
            for x in range(7, 11): put(x, 33, 'pele')         # mãos no colo
            for x in range(17, 21): put(x, 33, 'pele')
    elif pose == 'bracos':
        for y in range(22, 26):                               # mangas nos ombros
            for x in (5, 6, 7): put(x, y, 'roupa')
            for x in (20, 21, 22): put(x, y, 'roupa')
    else:                                                     # palmas
        for y in range(23, 29):
            for x in (5, 6, 7): put(x, y, 'roupa' if y < 26 else 'pele')
            for x in (20, 21, 22): put(x, y, 'roupa' if y < 26 else 'pele')
        if not costas:
            for x in range(8, 20):
                for y in range(27, 30): put(x, y, 'pele')
    im = Image.new('RGBA', (W, H)); px = im.load()
    rampas = {'pele': pele, 'roupa': roupa, 'calca': calca}
    xs = [x for (x, y) in m]; cx = (min(xs) + max(xs)) / 2
    for (x, y), parte in m.items():
        r = rampas[parte]
        t = 0 if x < cx - 3 else (2 if x > cx + 3 else 1)    # luz da esquerda
        if (x, y + 1) not in m or m.get((x, y + 1)) != parte: t = max(t, 1)
        if parte == 'roupa' and (x - 1, y) in m and m[(x - 1, y)] == 'pele': t = 2
        px[x, y] = r[t] + (255,)
    # dobras: linha escura entre braço e tronco
    for (x, y), parte in m.items():
        if parte == 'roupa' and y > 23 and ((x - 1, y) not in m or (x + 1, y) not in m): pass
    for (x, y) in list(m):
        for a, b in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            q = (x + a, y + b)
            if q not in m and 0 <= q[0] < W and 0 <= q[1] < H and not px[q][3]: px[q] = OUT + (255,)
    for y in range(23, 33):                                   # separa braço do tronco
        for x in (7, 8, 19, 20):
            if m.get((x, y)) in ('pele', 'roupa') and m.get((x + (1 if x < 14 else -1), y)) and m.get((x, y)) != m.get((x + (1 if x < 14 else -1), y)):
                pass
    return im
def bracos_no_ar(pele, roupa):
    """braços levantados por fora da cabeça (camada que fica por cima da cabeça)"""
    m = {}
    for y in range(5, 24):
        for x in (2, 3, 4): m[(x - (1 if y < 12 else 0), y)] = 'roupa' if y > 19 else 'pele'
        for x in (23, 24, 25): m[(x + (1 if y < 12 else 0), y)] = 'roupa' if y > 19 else 'pele'
    for x in range(0, 5):
        for y in range(2, 6): m[(x, y)] = 'pele'
    for x in range(23, 28):
        for y in range(2, 6): m[(x, y)] = 'pele'
    im = Image.new('RGBA', (W, H)); px = im.load()
    for (x, y), p in m.items():
        r = pele if p == 'pele' else roupa
        t = 0 if x < 3 or (14 < x < 25) else 2
        px[x, y] = r[min(2, t)] + (255,)
    for (x, y) in list(m):
        for a, b in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            q = (x + a, y + b)
            if q not in m and 0 <= q[0] < W and 0 <= q[1] < H: px[q] = OUT + (255,)
    return im
def corpo_lado(roupa, calca, pele):
    """sentado de perfil, virado para a direita: tronco estreito, braço à frente, coxas para a frente"""
    m = {}
    def put(x, y, parte): m[(x, y)] = parte
    for y in range(20, 23):
        for x in range(12, 16): put(x, y, 'pele')
    for y in range(22, 35):
        for x in range(10, 18): put(x, y, 'roupa')
    for y in range(33, 37):
        for x in range(10, 23): put(x, y, 'calca')
    for y in range(23, 30):                                   # braço ao longo do tronco
        for x in range(13, 17): put(x, y, 'braco' if y < 26 else 'pele')
    for y in range(29, 32):                                   # antebraço para a frente, mão no joelho
        for x in range(15, 22): put(x, y, 'pele')
    im = Image.new('RGBA', (W, H)); px = im.load()
    rampas = {'pele': pele, 'roupa': roupa, 'calca': calca, 'braco': roupa}
    for (x, y), parte in m.items():
        r = rampas[parte]
        t = 1
        if parte in ('roupa', 'calca') and x <= 11: t = 0
        if parte in ('roupa', 'calca') and x >= 16: t = 2
        if parte == 'braco': t = 0 if x == 13 else 1
        if parte == 'pele' and y >= 29: t = 0 if y == 29 else (2 if y == 31 else 1)
        px[x, y] = r[t] + (255,)
    for (x, y) in m:                                          # braço separado do tronco por uma linha escura
        if m[(x, y)] in ('braco', 'pele') and m.get((x - 1, y)) == 'roupa' and 23 <= y < 29: px[x - 1, y] = roupa[2] + (255,)
    for (x, y) in list(m):
        for a, b in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            q = (x + a, y + b)
            if q not in m and 0 <= q[0] < W and 0 <= q[1] < H and not px[q][3]: px[q] = OUT + (255,)
    return im
def limpa(im):
    """tapa buracos de 1 píxel e tira pontos pretos soltos"""
    px = im.load()
    for _ in range(2):
        for y in range(1, H - 1):
            for x in range(1, W - 1):
                n4 = [px[x - 1, y], px[x + 1, y], px[x, y - 1], px[x, y + 1]]
                cheios = [q for q in n4 if q[3]]
                if not px[x, y][3] and len(cheios) >= 3:
                    claros = [q for q in cheios if sum(q[:3]) >= 60]
                    px[x, y] = (min(claros, key=lambda q: sum(q[:3])) if claros else cheios[0])
                elif px[x, y][3] and sum(px[x, y][:3]) < 60:
                    viz = sum(1 for a in (-1, 0, 1) for b in (-1, 0, 1) if (a or b) and px[x + a, y + b][3])
                    if viz <= 1: px[x, y] = (0, 0, 0, 0)
    return im
def fa(fonte, pose, costas, roupa, calca, lado=None):
    frente, tras, dir34, esq34 = fonte
    # de lado: a cabeça a 3/4 (vistas 2 e 8), virada para o ringue; de perfil as luvas tapam o queixo dos atletas
    src = (dir34 if lado == 'dir' else esq34) if lado else (tras if costas else frente)
    head, rampa, hh = cabeca(src)
    im = corpo(pose, costas, roupa, calca, rampa)
    im.alpha_composite(head, (0, 21 - hh))                    # primeiro a camisola e o pescoço, depois a cabeça recortada por cima
    if pose == 'bracos': im.alpha_composite(bracos_no_ar(rampa, roupa))
    return limpa(im)
if __name__ == '__main__':
    F = fontes(); print('cabeças:', len(F))
    random.seed(3)
    amostra = [(0, 'sentado', 0, 1), (1, 'bracos', 0, 0), (2, 'palmas', 0, 5), (3, 'sentado', 0, 4), (min(4, len(F)-1), 'sentado', 1, 2), (min(5, len(F)-1), 'bracos', 1, 6)]
    Z = 8; out = Image.new('RGBA', (48*Z*len(amostra) + 40*Z + 20, 64*Z), (60, 60, 70, 255))
    atleta = Image.open(os.path.join(CAB, 'variantes', '00-corpo-base', 'south-west.png')).convert('RGBA')
    out.alpha_composite(atleta.resize((40*Z, 60*Z), Image.NEAREST), (0, 0))
    for i, (fi, pose, costas, ri) in enumerate(amostra):
        f = fa(F[fi], pose, costas, ROUPA[ri], CALCA[i % 3])
        out.alpha_composite(f.resize((W*Z, H*Z), Image.NEAREST), (40*Z + 20 + i*48*Z//1, 20*Z))
    out.save(sys.argv[1] if len(sys.argv) > 1 else os.path.join(AQUI, 'amostra.png'))
