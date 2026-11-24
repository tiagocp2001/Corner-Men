# Direto (mão direita, guarda ortodoxa) por esqueleto na PixelLab, com base em docs/pesquisa-direto.md.
# O golpe vai para onde o boneco OLHA em cada vista (como no jab: jab_vistas.desvio).
# Uso: python3 -I direto.py <vista 1-8> <nomes das versões...>   ex.: direto.py 2 a b
import json, math, os, re, subprocess, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, '..', 'pixellab-jab'))
import jab_vistas as J
RS = [0.071, 0.023, 0.217]                       # ombro direito (medidas da PixelLab)
R0 = [0.031, 0.134, 0.161]                       # luva direita na guarda
K = [0.05, 0.25, 0.65, 1, 1, 0.55, 0.2, 0.03]    # quanto o braço já fez: arranque, rotação, extensão, impacto (x2), regresso, regresso, guarda
HIPS = [5, 12, 18, 20, 20, 14, 6, 1]             # + = lado direito para a frente (máx. 20 no motor; a mão longe faz rodar mais)
CHEST = [-1, 10, 20, 20, 20, 15, 7, 1]           # o peito começa com uma pequena carga para trás
LEAN = [[1, 0], [2, -1], [4, -3], [6, -4], [6, -4], [4, -3], [2, -1], [0, 0]]   # para a frente e por cima da perna da frente
PEL = [[-0.002, 0.003, -0.002], [-0.006, 0.008, -0.004], [-0.010, 0.013, -0.006], [-0.012, 0.016, -0.007],
       [-0.012, 0.016, -0.007], [-0.008, 0.010, -0.005], [-0.003, 0.004, -0.002], [0, 0, 0]]
NOD = [1, 2, 4, 5, 5, 3, 1, 0]
def rot(v, th):                                   # roda [direita, frente] para a esquerda dele
    return [v[0] * math.cos(th) - v[1] * math.sin(th), v[0] * math.sin(th) + v[1] * math.cos(th)]
def pedido(k):
    th = math.radians(J.desvio(k)); s = J.desvio(k) / 45
    alvo = rot([0.0, float(os.environ.get('ALCANCE', 0.25))], th) + [0.22]          # cabeça do adversário, em frente ao olhar (um pouco além do alcance: o corpo roda)
    P = []
    for i in range(8):
        f = K[i]; pr = rot(PEL[i][:2], th)
        P.append({'frame': i + 1, 'pelvis': [round(pr[0], 4), round(pr[1], 4), PEL[i][2]], 'hips': HIPS[i], 'chest': CHEST[i],
                  'lean': LEAN[i], 'head': [round(8 * s), NOD[i]],
                  'right_hand': [round(R0[j] + (alvo[j] - R0[j]) * f, 3) for j in range(3)],
                  'left_hand': [-0.083, 0.09, 0.2],                     # a luva da frente volta para a cara
                  'right_elbow': [0.3, 0, -1] if f < 0.6 else [0.5, 0.1, -0.6], 'left_elbow': [-0.3, 0, -1],
                  'right_foot': [round(-0.012 * f, 3), round(0.008 * f, 3), 0]})   # o pé de trás gira para dentro (aproximação)
    return dict(character_id=J.CHAR, mode='skeleton-v3', directions=[J.ORD[k][0]], frame_count=8, poses=P,
                action_description='boxer throws a straight right hand (cross) from an orthodox guard: rear foot pivots, hips and shoulders rotate, left glove back to the face')
def verifica(req, k):
    h = req['poses'][3]['right_hand']; a = math.degrees(math.atan2(-h[0], h[1]))
    return abs(a - J.desvio(k)) < 3, round(a)
if __name__ == '__main__':
    k = int(sys.argv[1]) - 1; nomes = sys.argv[2:] or ['a']
    req = pedido(k); ok, a = verifica(req, k)
    print(f'vista {k + 1}: direto a {a}° (o olhar está a {J.desvio(k)}°)', 'OK' if ok else 'ERRADO')
    if not ok: sys.exit(1)
    if os.environ.get('SO_VERIFICA'): sys.exit(0)
    for n in nomes:
        r = dict(req); r['animation_name'] = f'Direto vista {k + 1} {n}'; print(J.mcp('animate_character', r).splitlines()[:1])
    for _ in range(len(nomes) + 1): J.mcp('wait_for_jobs', {'timeout_seconds': 300})
    t = J.mcp('get_character', {'character_id': J.CHAR}); d = J.ORD[k][0]
    for n in nomes:
        i = t.find(f'Direto vista {k + 1} {n}'); m = re.search(d + r': (https://backblaze\S+\{i\}\.png\S*) \(i=0\.\.(\d+)\)', t[i:])
        pasta = os.path.join(AQUI, f'{d}-direto-{n}'); os.makedirs(pasta, exist_ok=True)
        for j in range(int(m.group(2)) + 1): subprocess.run(['curl', '-sS', '--retry', '5', '--retry-all-errors', '-o', os.path.join(pasta, f'{j}.png'), m.group(1).replace('{i}', str(j))], check=True)
        json.dump(req, open(os.path.join(pasta, 'pedido.json'), 'w')); print('feita', pasta)
