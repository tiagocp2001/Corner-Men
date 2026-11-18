# Andar em guarda (deslocar com os pés, estilo boxe): o pé da frente avança, o corpo vai atrás e o de trás junta-se.
# Animação no sítio; no jogo o boneco desloca-se enquanto ela corre. Por peças: corpo (acima das coxas) + cada perna.
# Uso: python3 andar.py <pasta-com-as-8-vistas> [...]  -> andar.gif
import sys, os
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import saltitar as S
AQUI = os.path.dirname(os.path.abspath(__file__))
# para onde fica a "frente" de cada vista, no ecrã (x, y)
FRENTE = {'1 Frente': (0, 1), '2 Frente-dir.': (1, 1), '3 Dir. 3/4': (1, 0), '4 Direita': (1, 0),
          '5 Costas-dir.': (1, -1), '6 Costas': (0, -1), '7 Esquerda': (-1, 0), '8 Frente-esq.': (-1, 1)}
# vistas em que as pernas se tocam: coluna onde começa a perna da direita (pernas, botas)
CORTE = {'4 Direita': (18, 18), '8 Frente-esq.': (18, 19)}
# (avanço da frente, levanta da frente, avanço de trás, levanta de trás, corpo avança, corpo sobe)
CICLO = [(0, 0, 0, 0, 0, 0), (1, 1, 0, 0, 0, 1), (2, 0, 0, 0, 1, 0),
         (1, 0, -1, 0, 0, 0), (1, 0, 0, 1, 0, 1), (0, 0, 0, 0, 0, 0)]
DUR = [100, 90, 110, 90, 90, 100]
def pernas(im, t):
    px = im.load(); K, A = S.marks(im); L0 = K - 1        # das coxas para baixo
    pts = {(x, y) for y in range(L0, 60) for x in range(40) if px[x, y][3]}
    if t in CORTE:
        cl, cb = CORTE[t]
        cut = lambda p: p[0] >= (cb if p[1] >= A else cl)
        cs = [[p for p in pts if not cut(p)], [p for p in pts if cut(p)]]
    else:
        cs = []; seen = set()
        for p in sorted(pts):
            if p in seen: continue
            st = [p]; c = []
            while st:
                q = st.pop()
                if q in seen or q not in pts: continue
                seen.add(q); c.append(q); x, y = q; st += [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
            if len(c) >= 8: cs.append(c)
        if len(cs) == 1: cs.append([])
    cs = sorted(cs, key=lambda c: -len(c))[:2]
    v = FRENTE[t]
    proj = lambda c: (sum(p[0]*v[0] + p[1]*v[1] for p in c) / len(c)) if c else -99
    frente, tras = sorted(cs, key=proj, reverse=True)
    return L0, frente, tras
def fotograma(im, info, passo, t):
    L0, fr, tr = info; v = FRENTE[t]; pi = im.load()
    af, lf, at, lt, ac, sc = passo
    out = Image.new('RGBA', im.size); po = out.load()
    def put(x, y, p):
        if 0 <= x < 40 and 0 <= y < 60 and p[3]: po[x, y] = p
    for y in range(L0):                                   # corpo
        for x in range(40):
            put(x + ac*v[0], y + ac*v[1] - sc, pi[x, y])
    legs = [(tr, at, lt), (fr, af, lf)]
    legs.sort(key=lambda l: max((p[1] for p in l[0]), default=0))   # a mais de baixo fica à frente
    for c, a, l in legs:                                  # a perna inclina: a coxa fica presa, o pé é que anda
        if not c: continue
        bot = max(p[1] for p in c); h = max(1, bot - L0)
        for (x, y) in sorted(c, key=lambda p: p[1]):
            f = (y - L0) / h
            put(x + round(a*v[0]*f), y + round(a*v[1]*f) - round(l*f), pi[x, y])
    return out
def gif(pastas, saida):
    f2 = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 18)
    INFO = {n: pernas(Image.open(os.path.join(S.BASE, n + '.png')).convert('RGBA'), t) for n, t in S.ORD}
    Z, PAD, LAB = 4, 4, 28; frames = []
    for passo in CICLO:
        fr = Image.new('RGBA', (40*8*Z, (60+PAD)*len(pastas)*Z + LAB), (60, 60, 70, 255)); dr = ImageDraw.Draw(fr)
        for k, (n, t) in enumerate(S.ORD):
            dr.text((k*40*Z+6, (60+PAD)*len(pastas)*Z+4), t, fill=(255, 220, 120), font=f2)
            v = FRENTE[t]; ac = passo[4]
            for r, pasta in enumerate(pastas):
                ox, oy = k*40*Z, r*(60+PAD)*Z
                cx = 20 + ac*v[0]
                dr.ellipse((ox+(cx-14)*Z, oy+57*Z, ox+(cx+14)*Z, oy+60*Z), fill=(38, 38, 46, 255))
                im = Image.open(os.path.join(pasta, n + '.png')).convert('RGBA')
                fr.alpha_composite(fotograma(im, INFO[n], passo, t).resize((40*Z, 60*Z), Image.NEAREST), (ox, oy))
        frames.append(fr.convert('RGB'))
    frames[0].save(saida, save_all=True, append_images=frames[1:], duration=DUR, loop=0)
if __name__ == '__main__':
    gif(sys.argv[1:] or [S.BASE], os.path.join(AQUI, 'andar.gif'))
