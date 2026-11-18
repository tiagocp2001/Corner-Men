# Guarda a saltitar (teste do método por peças): 6 fotogramas, 8 vistas, corpo f + cabeças por cima.
# Uso: python3 saltitar.py <pasta-com-as-8-vistas> [<outra pasta> ...]  -> guarda-saltitar.gif
import sys, os, json
from PIL import Image, ImageDraw, ImageFont
AQUI = os.path.dirname(os.path.abspath(__file__))
CAB = os.path.join(AQUI, '..', 'cabecas-pixellab')
ORD = json.load(open(os.path.join(CAB, 'ordem-vistas.json')))       # [nome PixelLab, "n.º Nome"]
BASE = os.path.join(CAB, 'variantes', '00-corpo-base')
# Pé que fica no chão nas pontas, por vista: 'auto' (pela forma da bota), -1 ponta à esquerda, +1 à direita,
# 'frente' (ponta virada para nós: a bota estica). Uma entrada por bota, da esquerda para a direita da imagem.
SPLIT = {'8 Frente-esq.': 19}   # vistas em que as duas botas se tocam: coluna onde começa a bota da direita
PES = {'1 Frente': [-1, 'frente'], '3 Dir. 3/4': [+1, +1], '7 Esquerda': [-1, -1]}   # as outras: 'auto'
def cls(p):
    if not p[3]: return '.'
    r, g, b = p[:3]
    if r + g + b < 90: return '#'
    if r > 110 and r > 2.2*g and r > b + 40: return 'r'
    if r > 190 and g > 190 and b > 190: return 'w'
    if abs(r-g) < 18 and abs(g-b) < 22 and r < 160: return 'g'
    return 's'
def marks(im):
    px = im.load(); last = None
    for y in range(36, 52):
        if sum(1 for x in range(40) if cls(px[x, y]) in 'rw') >= 2: last = y
    K = last + 2
    A = next(y for y in range(K+1, 58) if sum(1 for x in range(40) if cls(px[x, y]) == 'g') >= 3)
    return K, A
def botas(im, A):
    px = im.load(); pts = {(x, y) for y in range(A, 60) for x in range(40) if px[x, y][3]}
    out = []; seen = set()
    for p in sorted(pts):
        if p in seen: continue
        st = [p]; c = []
        while st:
            q = st.pop()
            if q in seen or q not in pts: continue
            seen.add(q); c.append(q); x, y = q; st += [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        if len(c) >= 8: out.append(c)
    return sorted(out, key=lambda c: min(x for x, _ in c))
def ponta(c, modo):
    bot = max(y for _, y in c)
    if modo == 'frente': return {(x, y) for x, y in c if y >= bot-1}
    bx = [x for x, y in c if y >= bot-1]; mid = sum(bx)/len(bx)
    if modo == 'auto':
        top = min(y for _, y in c); tx = [x for x, y in c if y <= top+1]
        modo = 1 if mid >= sum(tx)/len(tx) else -1
    return {(x, y) for x, y in c if y >= bot-2 and (x-mid)*modo >= 0}
def sobe(im, dy):
    out = Image.new('RGBA', im.size); out.alpha_composite(im, (0, -dy)); return out
def agacha(im, K):
    out = Image.new('RGBA', im.size); po, pi = out.load(), im.load()
    for y in range(60):
        for x in range(40):
            if y > K: po[x, y] = pi[x, y]
            elif y >= 1: po[x, y] = pi[x, y-1]
    return out
def pontas(im, toes, ar):
    out = sobe(im, 1); po, pi = out.load(), im.load()
    for t in toes:
        for p in t: po[p] = pi[p]
    return sobe(out, 1) if ar else out
SEQ = ['chao', 'agacha', 'pontas', 'ar', 'pontas', 'agacha']; DUR = [90, 100, 80, 110, 80, 100]
def info():
    r = {}
    for n, t in ORD:
        im = Image.open(os.path.join(BASE, n + '.png')).convert('RGBA'); K, A = marks(im); cs = botas(im, A)
        if t in SPLIT and len(cs) == 1:
            sx = SPLIT[t]; cs = [[p for p in cs[0] if p[0] < sx], [p for p in cs[0] if p[0] >= sx]]
        modos = PES.get(t, ['auto'] * len(cs))
        r[n] = (K, [ponta(c, m) for c, m in zip(cs, modos)])
    return r
def fotograma(im, K, toes, kind):
    if kind == 'chao': return im.copy()
    if kind == 'agacha': return agacha(im, K)
    return pontas(im, toes, kind == 'ar')
def gif(pastas, saida):
    I = info(); f2 = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 18)
    Z, PAD, LAB = 4, 4, 28; frames = []
    for kind in SEQ:
        lift = 1 if kind == 'ar' else 0
        fr = Image.new('RGBA', (40*8*Z, (60+PAD)*len(pastas)*Z + LAB), (60, 60, 70, 255)); dr = ImageDraw.Draw(fr)
        for k, (n, t) in enumerate(ORD):
            dr.text((k*40*Z+6, (60+PAD)*len(pastas)*Z+4), t, fill=(255, 220, 120), font=f2)
            for r, pasta in enumerate(pastas):
                ox, oy = k*40*Z, r*(60+PAD)*Z; w = 14 - 2*lift
                dr.ellipse((ox+(20-w)*Z, oy+57*Z, ox+(20+w)*Z, oy+60*Z), fill=(38, 38, 46, 255))
                im = Image.open(os.path.join(pasta, n + '.png')).convert('RGBA')
                fr.alpha_composite(fotograma(im, *I[n], kind).resize((40*Z, 60*Z), Image.NEAREST), (ox, oy))
        frames.append(fr.convert('RGB'))
    frames[0].save(saida, save_all=True, append_images=frames[1:], duration=DUR, loop=0)
if __name__ == '__main__':
    gif(sys.argv[1:] or [BASE], os.path.join(AQUI, 'guarda-saltitar.gif'))
