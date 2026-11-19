# Caras novas para os fãs, desenhadas de raiz no estilo dos atletas: contorno de 1 píxel, 3 tons com luz da esquerda,
# olhos grandes pretos com brilho, sobrancelhas grossas, cabelo em madeixas. 16 de largura (um pouco menores que os atletas).
import random
from PIL import Image
OUT = (10, 8, 10)
PELES = [((252, 214, 176), (236, 176, 136), (204, 128, 96)), ((248, 190, 140), (228, 150, 108), (190, 104, 74)),
         ((222, 156, 104), (188, 118, 76), (146, 82, 54)), ((184, 112, 80), (146, 80, 56), (106, 54, 38)),
         ((150, 92, 62), (114, 64, 42), (80, 42, 28))]
CABELOS = [((74, 62, 58), (38, 30, 28), (16, 12, 12)), ((132, 92, 60), (92, 62, 40), (58, 38, 26)),
           ((176, 128, 76), (134, 92, 52), (94, 62, 36)), ((240, 212, 128), (210, 172, 86), (164, 126, 58)),
           ((214, 118, 62), (172, 82, 44), (124, 54, 30)), ((222, 222, 222), (176, 176, 180), (126, 126, 132))]
ESTILOS = ['curto', 'rapado', 'careca', 'caracois', 'comprido', 'rabo', 'bone', 'franja', 'curto', 'rapado']
W, H = 16, 19
# contorno da cabeça (cara) por linha: (x0, x1) de pele
FORMA = {2: (5, 10), 3: (4, 11), 4: (3, 12), 5: (3, 12), 6: (2, 13), 7: (2, 13), 8: (2, 13), 9: (2, 13), 10: (2, 13),
         11: (3, 12), 12: (3, 12), 13: (4, 11), 14: (5, 10), 15: (6, 9)}
def cabelo_mask(estilo, vista):
    m = set()
    cara = {(x, y) for y, (a, b) in FORMA.items() for x in range(a, b + 1)}
    def topo(lim, lados=0, sobe=0):
        s = {(x, y) for (x, y) in cara if y <= lim}
        if lados: s |= {(x, y) for (x, y) in cara if y <= lim + lados and (x <= 3 or x >= 12)}
        for k in range(1, sobe + 1):                         # volume por cima da cabeça
            a, b = FORMA[2]
            s |= {(x, 2 - k) for x in range(a + k - 1, b - k + 2)}
        return s
    if vista == 'costas':
        if estilo == 'careca': return set()
        if estilo == 'rapado': return topo(9)
        if estilo == 'bone': return {(x, y) for (x, y) in cara if 6 <= y <= 11}
        m = topo(12, 0, 2 if estilo == 'caracois' else 1)
        if estilo == 'comprido': m |= {(x, y) for x in range(2, 14) for y in range(12, 18)}
        if estilo == 'rabo': m |= {(x, y) for x in (7, 8) for y in range(12, 18)}
        return m
    if estilo == 'careca': return {(x, y) for (x, y) in cara if 7 <= y <= 9 and (x <= 2 or x >= 13)}
    if estilo == 'rapado': m = topo(4, 2)
    elif estilo == 'curto': m = topo(5, 2, 1)
    elif estilo == 'franja': m = topo(6, 2, 1)
    elif estilo == 'caracois': m = topo(5, 3, 2) | {(1, y) for y in range(5, 10)} | {(14, y) for y in range(5, 10)}
    elif estilo == 'comprido': m = topo(5, 2, 1) | {(x, y) for x in (1, 2, 13, 14) for y in range(6, 18)}
    elif estilo == 'rabo': m = topo(5, 2, 1)
    elif estilo == 'bone': m = {(x, y) for (x, y) in cara if 6 <= y <= 7 and (x <= 3 or x >= 12)}
    if vista == 'dir':                                        # 3/4 virado para a direita: cabelo cobre mais o lado esquerdo
        m |= {(x, y) for (x, y) in cara if x <= 4 and y <= 10 and estilo not in ('careca', 'bone', 'rapado')}
        m = {(x, y) for (x, y) in m if not (x >= 13 and y >= 7)}
        if estilo == 'rabo': m |= {(1, y) for y in range(6, 15)} | {(2, y) for y in range(6, 15)}
        if estilo == 'comprido': m = {(x, y) for (x, y) in m if x < 13}
    return m
def cara(pele, cab, estilo, barba, vista, mulher=False, bone=((222, 64, 54), (182, 38, 38), (124, 26, 30))):
    im = Image.new('RGBA', (W, H)); p = im.load()
    pix = {(x, y): 'pele' for y, (a, b) in FORMA.items() for x in range(a, b + 1)}
    if vista in ('frente', 'costas'):
        for y in (8, 9, 10): pix[(1, y)] = 'orelha'; pix[(14, y)] = 'orelha'
    elif vista == 'dir':
        for y in (8, 9, 10): pix[(3, y)] = 'orelha'
    for h in cabelo_mask(estilo, vista): pix[h] = 'cabelo'
    if estilo == 'bone' and vista != 'costas':
        for y in range(1, 6):
            if y in FORMA:
                for x in range(FORMA[y][0], FORMA[y][1] + 1): pix[(x, y)] = 'bone'
        for x in range(4, 12): pix[(x, 1)] = 'bone'
        for x in (range(2, 14) if vista == 'frente' else range(7, 16)): pix[(x, 6)] = 'aba'
    if estilo == 'bone' and vista == 'costas':
        for y in range(1, 7):
            if y in FORMA:
                for x in range(FORMA[y][0], FORMA[y][1] + 1): pix[(x, y)] = 'bone'
        for x in range(4, 12): pix[(x, 1)] = 'bone'
    if barba and vista != 'costas':
        for (x, y), k in list(pix.items()):
            if k == 'pele' and y >= 12 and (vista == 'frente' or x >= 5): pix[(x, y)] = 'barba'
            if k == 'pele' and y == 11 and x in ((3, 12) if vista == 'frente' else (12,)): pix[(x, y)] = 'barba'
    R = {'pele': pele, 'orelha': pele, 'cabelo': cab, 'barba': cab, 'bone': bone, 'aba': bone}
    for (x, y), k in pix.items():
        r = R[k]; t = 1
        if k in ('pele', 'orelha'):
            if x <= 4 and y <= 11: t = 0
            if x >= 11 or y >= 14: t = 2
            if k == 'orelha': t = 1 if x < 8 else 2
        elif k in ('cabelo', 'barba'):
            t = 1
            if (x - y) % 4 == 0: t = 0                       # madeixas claras na diagonal
            if (x + 2 * y) % 5 == 0: t = 2
            if x >= 12 or (y >= 11 and k == 'cabelo'): t = 2
        elif k == 'bone': t = 0 if x <= 5 else (2 if x >= 11 else 1)
        else: t = 2
        p[x, y] = r[t] + (255,)
    if vista != 'costas':                                     # cara
        if vista == 'frente': olhos = (4, 10); nariz = 8; boca = (6, 9)
        else: olhos = (6, 11); nariz = 12; boca = (9, 11)
        sob = cab[2] if estilo not in ('careca',) else pele[2]
        for ex in olhos:
            for y in (8, 9, 10): p[ex, y] = OUT + (255,); p[ex + 1, y] = OUT + (255,)
            p[ex + 1, 8] = (250, 250, 250, 255)              # brilho
            for x in (ex - 1, ex, ex + 1):
                if (x, 7) in pix: p[x, 7] = sob + (255,)     # sobrancelha grossa
        if vista == 'dir': p[olhos[1] + 1, 9] = pele[2] + (255,)
        p[nariz, 11] = pele[2] + (255,); p[nariz, 12] = pele[2] + (255,)
        lab = (196, 84, 80) if mulher else tuple(int(v * .78) for v in pele[2])
        for x in range(boca[0], boca[1]):
            if pix.get((x, 13)) in ('pele', 'barba'): p[x, 13] = lab + (255,)
    for (x, y) in list(pix):                                  # contorno de 1 píxel por fora
        for a, b in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            q = (x + a, y + b)
            if q not in pix and 0 <= q[0] < W and 0 <= q[1] < H and not p[q][3]: p[q] = OUT + (255,)
    return im
def gerar(n, seed=1):
    random.seed(seed); out = []
    for i in range(n):
        estilo = random.choice(ESTILOS); mulher = estilo in ('comprido', 'rabo')
        cab = random.choice(CABELOS[:5]) if random.random() < .88 else CABELOS[5]
        out.append(dict(pele=random.choice(PELES), cab=cab, estilo=estilo, barba=(not mulher) and random.random() < 0.25, mulher=mulher))
    return out
def vistas(d):
    f = cara(d['pele'], d['cab'], d['estilo'], d['barba'], 'frente', d['mulher'])
    c = cara(d['pele'], d['cab'], d['estilo'], d['barba'], 'costas', d['mulher'])
    r = cara(d['pele'], d['cab'], d['estilo'], d['barba'], 'dir', d['mulher'])
    return f, c, r, r.transpose(Image.FLIP_LEFT_RIGHT)
if __name__ == '__main__':
    import sys
    D = gerar(8, 11); Z = 12
    out = Image.new('RGBA', (8 * 18 * Z + 44 * Z, 4 * 21 * Z), (60, 60, 70, 255))
    atl = Image.open('/home/user/Corner-Men/arte/cabecas-pixellab/variantes/00-corpo-base/south-west.png').convert('RGBA').crop((0, 0, 40, 28))
    out.alpha_composite(atl.resize((40 * Z, 28 * Z), Image.NEAREST), (0, 0))
    for i, d in enumerate(D):
        for r, v in enumerate(vistas(d)):
            out.alpha_composite(v.resize((W * Z, H * Z), Image.NEAREST), (44 * Z + i * 18 * Z, r * 21 * Z))
    out.save(sys.argv[1])
