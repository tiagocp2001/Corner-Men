# Guarda (idle) por esqueleto na PixelLab, com base no nosso saltitar: dois saltinhos nas pontas dos pés
# e o peso a passar de um lado para o outro (um salto para a direita, o seguinte para a esquerda).
import json, os, re, subprocess, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, '..', 'pixellab-jab'))
import jab_vistas as J
UP   = [-0.010, 0.000, 0.014, 0.000, -0.010, 0.000, 0.014, 0.000]   # agacha, sobe, no ar, aterra (x2)
LIFT = [0, 0, 0.014, 0, 0, 0, 0.014, 0]                            # no ar os dois pés saem do chão
SIDE = [0.006, 0.012, 0.012, 0.006, -0.006, -0.012, -0.012, -0.006]  # peso: direita no 1.º salto, esquerda no 2.º
P = []
for i in range(8):
    q = {'frame': i + 1, 'pelvis': [SIDE[i], 0, UP[i]], 'lean': [0, round(SIDE[i] * 150)], 'head': [0, 1 if UP[i] < 0 else 0]}
    if LIFT[i]: q['right_foot'] = [0, 0, LIFT[i]]; q['left_foot'] = [0, 0, LIFT[i]]
    P.append(q)
req = dict(character_id=J.CHAR, mode='skeleton-v3', directions=['south', 'east'], frame_count=8, poses=P,
           animation_name='Guarda saltitar',
           action_description='boxer in guard bouncing lightly on the balls of his feet, shifting his weight from one leg to the other, gloves up')
print(J.mcp('animate_character', req)[:400])
for _ in range(3): J.mcp('wait_for_jobs', {'timeout_seconds': 300})
t = J.mcp('get_character', {'character_id': J.CHAR}); i = t.find('Guarda saltitar')
for d in ['south', 'east']:
    m = re.search(d + r': (https://backblaze\S+\{i\}\.png\S*) \(i=0\.\.(\d+)\)', t[i:])
    pasta = os.path.join(AQUI, d); os.makedirs(pasta, exist_ok=True)
    for j in range(int(m.group(2)) + 1): subprocess.run(['curl', '-sS', '-o', os.path.join(pasta, f'{j}.png'), m.group(1).replace('{i}', str(j))], check=True)
json.dump(req, open(os.path.join(AQUI, 'pedido.json'), 'w'))
print('feito')
