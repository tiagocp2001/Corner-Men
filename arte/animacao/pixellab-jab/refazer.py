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
pedidos = [(0, 'p1', preso(55)), (0, 'p2', preso(55))]
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
