# Levar um soco na cara (jab ou direto, vindo de frente) por esqueleto na PixelLab, a partir de docs/pesquisa-levar-golpe.md.
# Os valores da pesquisa são reais; aqui vão aumentados (EXAG) porque num boneco de 40x60 um movimento real quase não se vê.
# O corpo recua para trás do OLHAR em cada vista (como no jab: jab_vistas.desvio).
# Uso: python3 -I levar.py <jab|direto> <vista 1-8> <versões...>
import json, math, os, re, subprocess, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, '..', 'pixellab-jab'))
import jab_vistas as J
EXAG = float(os.environ.get('EXAG', 2.5))
EXAG_CAB = float(os.environ.get('EXAG_CAB', EXAG))     # a cabeça aumentada demais fica deformada (o queixo para o céu)
# (cabeça rot [+ = nariz p/ direita], cabeça incl [- = queixo p/ cima], tronco frente, pelvis dz ×H, pelvis dy ×H) — tabelas da pesquisa
T = {'jab':    [(0, 3, 0, 0, 0), (-2, -3, -1, -0.002, 0), (-3, -6, -2, -0.004, -0.002), (-2, -4, -2, -0.005, -0.003),
                (-1, -1, -1, -0.003, -0.002), (0, 2, 0, -0.001, -0.001), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0)],
     'direto': [(0, 2, 0, 0, 0), (6, -8, -1, -0.003, 0), (14, -22, -4, -0.008, -0.004), (10, -16, -7, -0.014, -0.008),
                (5, -9, -6, -0.016, -0.010), (2, -3, -3, -0.010, -0.006), (0, 3, 1, -0.004, -0.002), (0, 0, 0, 0, 0)]}
H = 0.5                                             # altura do corpo nas unidades da PixelLab (pelvis a 0,228 do chão)
def rot(v, th): return [v[0] * math.cos(th) - v[1] * math.sin(th), v[0] * math.sin(th) + v[1] * math.cos(th)]
def pedido(g, k):
    th = math.radians(J.desvio(k)); P = []
    for i, (hr, hi, tf, dz, dy) in enumerate(T[g]):
        pz = rot([0, dz * H * EXAG], th)            # recua para trás do olhar
        P.append({'frame': i + 1, 'pelvis': [round(pz[0], 4), round(pz[1], 4), round(dy * H * EXAG, 4)],
                  'lean': [round(tf * EXAG, 1), 0], 'head': [round(-hr * EXAG_CAB + (8 * J.desvio(k) / 45)), round(hi * EXAG_CAB)],
                  'hips': 0, 'chest': 0})
    return dict(character_id=J.CHAR, mode='skeleton-v3', directions=[J.ORD[k][0]], frame_count=8, poses=P,
                action_description='boxer in guard recoils as if rocked: head snaps back with the chin up, the upper body leans back a little, then he recovers to the same guard; feet stay planted. Draw only this one boxer and nothing else: no other arms, hands or gloves, no punch, no effects, no motion lines, no particles; the face keeps the same features, eyes open, serious')
def verifica(req, k):
    """o corpo tem de recuar para trás do olhar: ângulo da pelvis no recuo máximo = desvio + 180°"""
    p = min(req['poses'], key=lambda q: q['pelvis'][1] * math.cos(math.radians(J.desvio(k))) - q['pelvis'][0] * math.sin(math.radians(J.desvio(k))))['pelvis']
    if abs(p[0]) + abs(p[1]) < 1e-6: return True, None
    a = math.degrees(math.atan2(-p[0], p[1])) % 360
    return abs(((a - (J.desvio(k) + 180)) + 180) % 360 - 180) < 3, round(a)
if __name__ == '__main__':
    g, k, nomes = sys.argv[1], int(sys.argv[2]) - 1, sys.argv[3:] or ['a']
    req = pedido(g, k); ok, a = verifica(req, k)
    print(f'{g} vista {k + 1}: recua a {a}° (para trás do olhar = {J.desvio(k) + 180}°)', 'OK' if ok else 'ERRADO')
    if not ok or os.environ.get('SO_VERIFICA'): sys.exit(0 if ok else 1)
    for n in nomes:
        r = dict(req); r['animation_name'] = f'Levar {g} vista {k + 1} {n}'; J.mcp('animate_character', r)
    for _ in range(len(nomes) + 1): J.mcp('wait_for_jobs', {'timeout_seconds': 300})
    t = J.mcp('get_character', {'character_id': J.CHAR}); d = J.ORD[k][0]
    for n in nomes:
        i = t.find(f'Levar {g} vista {k + 1} {n}'); m = re.search(d + r': (https://backblaze\S+\{i\}\.png\S*) \(i=0\.\.(\d+)\)', t[i:])
        pasta = os.path.join(AQUI, f'{d}-{g}-{n}'); os.makedirs(pasta, exist_ok=True)
        for j in range(int(m.group(2)) + 1): subprocess.run(['curl', '-sS', '--retry', '5', '--retry-all-errors', '-o', os.path.join(pasta, f'{j}.png'), m.group(1).replace('{i}', str(j))], check=True)
        json.dump(req, open(os.path.join(pasta, 'pedido.json'), 'w')); print('feita', pasta)
