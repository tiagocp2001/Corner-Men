# Guarda com mais vida: o saltitar (saltitar.py, com os pés escolhidos por vista) +
#  - luvas com um pequeno atraso em relação ao corpo (1 píxel);
#  - peso a passar de uma perna para a outra (o corpo de cima desvia 1 píxel para um lado e depois para o outro).
# Uso: python3 guarda.py <pasta-com-as-8-vistas> [...]  -> guarda.gif
import sys, os
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import saltitar as S
AQUI = os.path.dirname(os.path.abspath(__file__))
# 12 fotogramas = 2 saltos: no 1.º o peso vai para a esquerda, no 2.º para a direita
PASSOS = ['chao', 'agacha', 'pontas', 'ar', 'pontas', 'agacha'] * 2
LUVA = [0, -1, +1, 0, -1, +1] * 2                 # luvas: ficam para trás quando o corpo muda de direção
PESO = [0, -1, -1, -1, -1, 0, 0, +1, +1, +1, +1, 0]  # desvio do corpo de cima (x), as botas ficam
DUR = S.DUR * 2
def luvas(im):
    """máscara das luvas: vermelho dos braços (acima dos calções), brancos e contorno colados"""
    px = im.load(); K, A = S.marks(im)
    top_short = next(y for y in range(30, 52) if sum(1 for x in range(40) if S.cls(px[x, y]) == 'w') >= 4)
    cand = {(x, y) for y in range(0, top_short - 1) for x in range(40) if S.cls(px[x, y]) == 'r'}
    red = set(); seen = set()
    for p in cand:                                   # só manchas grandes (a boca e pontos da cara ficam de fora)
        if p in seen: continue
        st = [p]; c = []
        while st:
            q = st.pop()
            if q in seen or q not in cand: continue
            seen.add(q); c.append(q); x, y = q; st += [(x+a, y+b) for a in (-1, 0, 1) for b in (-1, 0, 1)]
        if len(c) >= 8: red |= set(c)
    m = set(red)
    for (x, y) in red:
        for a in (-1, 0, 1):
            for b in (-1, 0, 1):
                q = (x + a, y + b)
                if 0 <= q[0] < 40 and 0 <= q[1] < 60 and S.cls(px[q]) in '#w': m.add(q)
    return m
def xdesvio(im, K, dx):
    """o que está acima da coxa (linha K) anda dx; as pernas de baixo ficam"""
    if not dx: return im
    out = Image.new('RGBA', im.size); po, pi = out.load(), im.load()
    for y in range(60):
        for x in range(40):
            if y > K: po[x, y] = pi[x, y]
            else:
                X = x - dx
                if 0 <= X < 40: po[x, y] = pi[X, y]
    return out
def mascara_img(m):
    im = Image.new('RGBA', (40, 60))
    for p in m: im.putpixel(p, (255, 255, 255, 255))
    return im
def fotograma(im, K, toes, kind, luva, peso, mlu):
    a = S.fotograma(xdesvio(im, K, peso), K, toes, kind)
    m = S.fotograma(xdesvio(mlu, K, peso), K, toes, kind)       # a máscara das luvas mexe igual ao corpo
    if not luva: return a
    out = a.copy(); po, pa, pm = out.load(), a.load(), m.load()
    M = {(x, y) for y in range(60) for x in range(40) if pm[x, y][3]}
    for (x, y) in M:                                            # o sítio que a luva deixa: pixel do lado de fora
        if (x, y - luva) not in M:
            Y = y - luva
            while (x, Y) in M: Y -= luva
            if 0 <= Y < 60: po[x, y] = pa[x, Y]
    for (x, y) in M:
        Y = y + luva
        if 0 <= Y < 60: po[x, Y] = pa[x, y]
    return out
def gif(pastas, saida):
    I = S.info(); f2 = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 18)
    ML = {n: mascara_img(luvas(Image.open(os.path.join(S.BASE, n + '.png')).convert('RGBA'))) for n, _ in S.ORD}
    Z, PAD, LAB = 4, 4, 28; frames = []
    for kind, lu, pe in zip(PASSOS, LUVA, PESO):
        lift = 1 if kind == 'ar' else 0
        fr = Image.new('RGBA', (40*8*Z, (60+PAD)*len(pastas)*Z + LAB), (60, 60, 70, 255)); dr = ImageDraw.Draw(fr)
        for k, (n, t) in enumerate(S.ORD):
            dr.text((k*40*Z+6, (60+PAD)*len(pastas)*Z+4), t, fill=(255, 220, 120), font=f2)
            for r, pasta in enumerate(pastas):
                ox, oy = k*40*Z, r*(60+PAD)*Z; w = 14 - 2*lift
                dr.ellipse((ox+(20-w+pe)*Z, oy+57*Z, ox+(20+w+pe)*Z, oy+60*Z), fill=(38, 38, 46, 255))
                im = Image.open(os.path.join(pasta, n + '.png')).convert('RGBA')
                K, toes = I[n]
                fr.alpha_composite(fotograma(im, K, toes, kind, lu, pe, ML[n]).resize((40*Z, 60*Z), Image.NEAREST), (ox, oy))
        frames.append(fr.convert('RGB'))
    frames[0].save(saida, save_all=True, append_images=frames[1:], duration=DUR, loop=0)
    return frames
if __name__ == '__main__':
    gif(sys.argv[1:] or [S.BASE], os.path.join(AQUI, 'guarda.gif'))
