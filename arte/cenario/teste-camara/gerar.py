# Gera as imagens do teste da câmara: pugilistas (guarda, 8 vistas x 12 fotogramas) e fãs.
import sys, os, random
from PIL import Image
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, '..', '..', 'animacao'))
import saltitar as S, guarda as G
def atlas(pasta, azul=False):
    I = S.info(); out = Image.new('RGBA', (40*12, 60*8))
    for r, (n, t) in enumerate(S.ORD):
        im = Image.open(os.path.join(pasta, n + '.png')).convert('RGBA')
        ml = G.mascara_img(G.luvas(Image.open(os.path.join(S.BASE, n + '.png')).convert('RGBA')))
        K, toes = I[n]
        for c, (kind, lu, pe) in enumerate(zip(G.PASSOS, G.LUVA, G.PESO)):
            f = G.fotograma(im, K, toes, kind, lu, pe, ml)
            if azul:
                px = f.load()
                for y in range(60):
                    for x in range(40):
                        p = px[x, y]
                        if p[3] and S.cls(p) == 'r':
                            px[x, y] = (int(p[0]*.16), int(p[0]*.42), min(255, int(p[0]*1.02)), 255)
            out.paste(f, (c*40, r*60))
    return out
# ---- fãs: 12x18, poses: 0 sentado, 1 braços no ar, 2 palmas (de frente); 3 sentado, 4 braços (de costas)
PELE = [(249,207,166),(233,165,127),(217,147,95),(184,112,70),(140,74,51),(104,50,35)]
CAB = [(30,24,22),(70,45,30),(120,80,45),(200,170,90),(150,60,30),(150,150,150)]
ROUPA = [(200,40,40),(40,80,190),(230,230,230),(40,40,46),(60,130,70),(220,170,40),(120,60,140),(90,90,100),(180,90,40),(30,110,130),(200,40,40),(40,80,190)]
OUT = (12,10,14)
def fa(pele, cab, roupa, pose, costas, careca):
    im = Image.new('RGBA', (12, 18)); p = im.load()
    def r(x0, y0, x1, y1, c):
        for y in range(y0, y1+1):
            for x in range(x0, x1+1):
                if 0 <= x < 12 and 0 <= y < 18: p[x, y] = c + (255,)
    sh = tuple(int(v*.72) for v in roupa); ps = tuple(int(v*.8) for v in pele)
    # tronco
    r(2, 9, 9, 17, OUT); r(3, 10, 8, 17, roupa); r(8, 10, 8, 17, sh)
    # cabeça
    r(3, 2, 8, 9, OUT); r(4, 3, 7, 8, pele); r(7, 4, 7, 8, ps)
    hc = pele if careca else cab
    if costas: r(4, 3, 7, 8, hc if not careca else pele); r(4, 8, 7, 8, ps)
    else:
        r(4, 3, 7, 3, hc); r(4, 4, 4, 4, hc)
        p[5, 6] = OUT + (255,); p[7, 6] = OUT + (255,)
    # braços (contorno por fora, manga/pele por dentro)
    if pose == 0:
        r(1, 10, 1, 16, OUT); r(10, 10, 10, 16, OUT); r(2, 10, 2, 15, sh); r(9, 10, 9, 15, sh)
        p[2, 16] = pele+(255,); p[9, 16] = pele+(255,)
    elif pose == 1:
        r(0, 0, 3, 10, OUT); r(8, 0, 11, 10, OUT); r(1, 1, 2, 9, pele); r(9, 1, 10, 9, pele)
        r(1, 7, 2, 9, roupa); r(9, 7, 10, 9, roupa)
    else:
        r(1, 10, 1, 14, OUT); r(10, 10, 10, 14, OUT); r(2, 10, 2, 13, sh); r(9, 10, 9, 13, sh)
        r(3, 12, 8, 14, OUT); r(4, 13, 7, 13, pele)
    return im
def fas():
    random.seed(7); N = 32; out = Image.new('RGBA', (12*N, 18*5))
    for c in range(N):
        pele = random.choice(PELE); cab = random.choice(CAB); roupa = random.choice(ROUPA); careca = random.random() < .12
        for row, (pose, costas) in enumerate([(0, 0), (1, 0), (2, 0), (0, 1), (1, 1)]):
            out.paste(fa(pele, cab, roupa, pose, costas, careca), (c*12, row*18))
    return out
if __name__ == '__main__':
    atlas(S.BASE).save(os.path.join(AQUI, 'lutador-a.png'))
    atlas(sys.argv[1], azul=True).save(os.path.join(AQUI, 'lutador-b.png'))
    fas().save(os.path.join(AQUI, 'fas.png'))
