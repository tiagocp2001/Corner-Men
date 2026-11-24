# Refaz vistas do jab em versões alternativas (para escolher). Uso: python3 -I refazer.py
import json, math, os, re, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import jab_vistas as J
def versao(k, nome, ajusta):
    req = J.pedido(k); ajusta(req); req['animation_name'] = f'Jab vista {k + 1} {nome}'
    h = req['poses'][3]['left_hand']; a = math.degrees(math.atan2(-(h[0] - J.LS[0]), h[1] - J.LS[1]))
    print(f'vista {k + 1} {nome}: jab a {a:.0f}° da frente do corpo para a PixelLab (o olhar está a {J.desvio(k)}°)')
    J.mcp('animate_character', req)
    return req
def direcao(gr):
    def f(req):
        th = math.radians(gr); I = [J.LS[0] - 0.19 * math.sin(th), J.LS[1] + 0.19 * math.cos(th), 0.228]
        for q, k in zip(req['poses'], J.K): q['left_hand'] = [round(J.R0[j] + (I[j] - J.R0[j]) * k, 3) for j in range(3)]
    return f
def preso(gr):
    d = direcao(gr)
    def f(req):
        d(req)
        for q in req['poses']:            # corpo preso: só o braço do jab se mexe
            q['chest'] = 0; q['hips'] = 0; q['head'] = [0, 0]; q['lean'] = [0, 0]; q['pelvis'] = [0, 0, 0]
    return f
def preso_cabeca(gr):
    d = preso(gr); base = J.pedido(0)['poses']
    def f(req):
        d(req)
        for q, b in zip(req['poses'], base): q['head'] = b['head']   # a cabeça mexe como na versão A (queixo a baixar e a acompanhar)
    return f
def so_cabeca(gr):
    d = preso(gr)
    NOD = [2, 4, 7, 10, 10, 7, 4, 1]; TURN = [3, 5, 8, 10, 10, 8, 5, 2]
    def f(req):
        d(req)
        for q, n, t in zip(req['poses'], NOD, TURN):
            q['head'] = [t, n]; q['right_hand'] = [0.06, 0.11, 0.19]; q['right_elbow'] = [0.3, 0, -1]
        req['action_description'] = 'boxer throws a quick left jab: only the left arm and the head move (chin tucks down behind the lead shoulder); the right glove stays still at the chin; body and legs do not move'
    return f
pedidos = [(0, 'h1', so_cabeca(55)), (0, 'h2', so_cabeca(55)), (0, 'h3', so_cabeca(55)), (0, 'h4', so_cabeca(55))]
feitos = [(k, n, versao(k, n, f)) for k, n, f in pedidos]
for _ in range(4): J.mcp('wait_for_jobs', {'timeout_seconds': 300})
t = J.mcp('get_character', {'character_id': J.CHAR})
for k, n, req in feitos:
    i = t.find(req['animation_name']); d = J.ORD[k][0]
    m = re.search(d + r': (https://backblaze\S+\{i\}\.png\S*) \(i=0\.\.(\d+)\)', t[i:])
    if not m: print('falta', k + 1, n); continue
    pasta = os.path.join(J.AQUI, f'{d}-jab-{n}'); os.makedirs(pasta, exist_ok=True)
    for j in range(int(m.group(2)) + 1): subprocess.run(['curl', '-sS', '-o', os.path.join(pasta, f'{j}.png'), m.group(1).replace('{i}', str(j))], check=True)
    json.dump(req, open(os.path.join(pasta, 'pedido.json'), 'w')); print('feita', pasta)
