# Verifica se o corpo de uma variante ficou igual ao corpo base (do peito para baixo).
# A cabeça, o cabelo e a barba ficam de fora (podem ocupar píxeis diferentes); a pele pode mudar de tom.
# Conta só o que importa para as animações e para pintar: forma (vazio/cheio) e onde estão as luvas,
# os calções (vermelho e branco) e as botas.
import sys, os
from PIL import Image
AQUI = os.path.dirname(os.path.abspath(__file__))
DIRS = ['south','south-east','east','north-east','north','north-west','west','south-west']
S = [28,26,24,25,27,26,25,26]    # linha dos ombros do corpo base em cada vista
FOLGA = 3                        # linhas abaixo dos ombros que ficam de fora (cabelo/barba a cair)
LIMITE = 3.0                     # % máxima de píxeis diferentes por vista
def cls(p):
    if not p[3]: return 'vazio'
    r, g, b = p[:3]
    if r + g + b < 90: return 'escuro'
    if r > 110 and r > 2.2*g and r > b + 40: return 'vermelho'
    if r > 190 and g > 190 and b > 190 and max(r, g, b) - min(r, g, b) < 30: return 'branco'   # branco dos calções (pele muito clara não conta)
    return 'pele'   # pele, sombras, botas cinzentas: o tom pode mudar
def verificar(pasta):
    res = []
    for k, d in enumerate(DIRS):
        a = Image.open(os.path.join(AQUI, 'variantes', '00-corpo-base', d + '.png')).convert('RGBA').load()
        b = Image.open(os.path.join(pasta, d + '.png')).convert('RGBA').load()
        tot = bad = 0
        for y in range(S[k] + FOLGA, 60):
            for x in range(40):
                ca, cb = cls(a[x, y]), cls(b[x, y])
                if ca == cb == 'vazio': continue
                tot += 1
                if ca != cb and ('vazio' in (ca, cb) or 'vermelho' in (ca, cb) or 'branco' in (ca, cb)): bad += 1
        res.append((d, 100*bad/max(tot, 1)))
    return res
if __name__ == '__main__':
    r = verificar(sys.argv[1])
    for d, p in r: print(f'{d:11s} {p:4.1f}%' + ('  <-- DIFERENTE' if p > LIMITE else ''))
    print('OK' if all(p <= LIMITE for _, p in r) else 'CORPO MUDOU')
