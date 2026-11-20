# Deslocar no ringue: a guarda a saltitar (guarda.py) + inclinação para onde vai + pés a aterrar desencontrados.
# A animação é no sítio; o jogo é que desloca o boneco. Esta é a versão "para a frente" de cada vista.
# Uso: python3 deslocar.py <pasta-com-as-8-vistas> [...]  -> deslocar-frente.gif
import sys, os
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import saltitar as S, guarda as G, andar as A
AQUI = os.path.dirname(os.path.abspath(__file__))
INCLINA = [0, 0, 1, 1, 1, 0] * 2      # no ar o corpo de cima vai 1 píxel para onde ele se desloca
TRAS_NO_AR = [0, 0, 0, 0, 1, 0] * 2   # a descer, o pé de trás ainda vem no ar (aterra depois do da frente)
def cintura(im):
    """linha de cima dos calções (o elástico branco)"""
    px = im.load()
    return next(y for y in range(30, 52) if sum(1 for x in range(40) if S.cls(px[x, y]) == 'w') >= 4)
def inclina(im, C, v, n):
    """o corpo dobra pela cintura (linha C) só para o lado para onde vai; calções e pernas ficam inteiros.
    Para a frente/para trás no ecrã (vistas de frente e de costas) não se mexe: não há linhas vazias."""
    if not n or not v[0]: return im
    out = Image.new('RGBA', im.size); po, pi = out.load(), im.load()
    for y in range(60):
        for x in range(40):
            if y >= C: po[x, y] = pi[x, y]
            else:
                X = x - n*v[0]
                if 0 <= X < 40: po[x, y] = pi[X, y]
    return out
def levanta(im, L0, perna, n):
    if not n or not perna: return im
    out = im.copy(); po, pi = out.load(), im.load()
    bot = max(p[1] for p in perna); h = max(1, bot - L0)
    for p in perna: po[p] = (0, 0, 0, 0)
    for (x, y) in sorted(perna, key=lambda p: p[1]):
        Y = y - round(n * (y - L0) / h)
        if 0 <= Y < 60: po[x, Y] = pi[x, y]
    return out
def gif(pastas, saida):
    I = S.info(); f2 = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 18)
    bases = {n: Image.open(os.path.join(S.BASE, n + '.png')).convert('RGBA') for n, _ in S.ORD}
    ML = {n: G.mascara_img(G.luvas(bases[n])) for n, _ in S.ORD}
    PE = {n: A.pernas(bases[n], t) for n, t in S.ORD}
    CI = {n: cintura(bases[n]) for n, _ in S.ORD}
    Z, PAD, LAB = 4, 4, 28; frames = []
    for i, (kind, lu) in enumerate(zip(G.PASSOS, G.LUVA)):
        lift = 1 if kind == 'ar' else 0
        fr = Image.new('RGBA', (40*8*Z, (60+PAD)*len(pastas)*Z + LAB), (60, 60, 70, 255)); dr = ImageDraw.Draw(fr)
        for k, (n, t) in enumerate(S.ORD):
            dr.text((k*40*Z+6, (60+PAD)*len(pastas)*Z+4), t, fill=(255, 220, 120), font=f2)
            v = A.FRENTE[t]; K, toes = I[n]; L0, frente, tras = PE[n]
            for r, pasta in enumerate(pastas):
                ox, oy = k*40*Z, r*(60+PAD)*Z; w = 14 - 2*lift; cx = 20 + INCLINA[i]*v[0]
                dr.ellipse((ox+(cx-w)*Z, oy+57*Z, ox+(cx+w)*Z, oy+60*Z), fill=(38, 38, 46, 255))
                im = Image.open(os.path.join(pasta, n + '.png')).convert('RGBA')
                im2 = levanta(inclina(im, CI[n], v, INCLINA[i]), L0, tras, TRAS_NO_AR[i])
                ml2 = inclina(ML[n], CI[n], v, INCLINA[i])
                fr.alpha_composite(G.fotograma(im2, K, toes, kind, lu, 0, ml2).resize((40*Z, 60*Z), Image.NEAREST), (ox, oy))
        frames.append(fr.convert('RGB'))
    frames[0].save(saida, save_all=True, append_images=frames[1:], duration=G.DUR, loop=0)
if __name__ == '__main__':
    gif(sys.argv[1:] or [S.BASE], os.path.join(AQUI, 'deslocar-frente.gif'))
