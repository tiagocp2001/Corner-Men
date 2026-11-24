# Jab por esqueleto na PixelLab, vista a vista, com o golpe virado para onde o boneco OLHA em cada vista.
# A PixelLab acha que o corpo f está virado para a sua direção (south, east...), mas no desenho o olhar está
# rodado (o jogo usa VANG). O jab roda essa diferença para o lado esquerdo dele (ver docs/pesquisa-jab.md).
# Uso: python3 -I jab_vistas.py   -> faz as vistas pendentes enquanto houver >= 3 gerações; refaz o atlas do ringue.
import json, math, os, re, subprocess, sys
from PIL import Image
import numpy as np
AQUI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(AQUI, '..', '..', '..'))
CAB = os.path.join(REPO, 'arte', 'cabecas-pixellab')
ATLAS = os.path.join(REPO, 'arte', 'cenario', 'teste-camara', 'jab-a.png')
LISTA = os.path.join(REPO, 'arte', 'cenario', 'teste-camara', 'jab-vistas.json')
EST = os.path.join(AQUI, 'estado.json')
CHAR = '71e97b6f-c6bd-4c1a-9f08-d3cda3086df0'          # cópia do corpo f com tela 72x64
ORD = json.load(open(os.path.join(CAB, 'ordem-vistas.json')))
VANG = [0, 45, 72, 100, 140, 195, 270, 315]
PL = {'south': 0, 'south-east': 45, 'east': 90, 'north-east': 135, 'north': 180, 'north-west': 225, 'west': 270, 'south-west': 315}
ORDEM = [5, 6, 0, 4, 7, 3, 2]                          # vistas por fazer (índice 0-7): mais vistas na luta primeiro; 3 = refazer a 4
LS = [-0.074, -0.022, 0.217]; R0 = [-0.16, 0.06, 0.178]   # ombro esquerdo e luva esquerda na guarda (medidas da PixelLab)
K = [0.15, 0.4, 0.7, 1, 1, 0.65, 0.3, 0.05]             # quanto o braço já fez em cada fotograma
def mcp(tool, args):
    out = subprocess.run([sys.executable, '-I', os.path.join(CAB, 'mcp.py'), tool, json.dumps(args)], capture_output=True, text=True).stdout
    d = json.loads(out, strict=False)['result']
    return '\n'.join(c.get('text', '') for c in d['content'] if c.get('type') == 'text')
def gerações():
    t = mcp('get_balance', {})
    h = re.search(r'generations_today: ([\d.]+)', t)
    return float(re.search(r'generations_remaining: ([\d.]+)', t).group(1)) + (float(h.group(1)) if h else 0)
def desvio(k):
    return (VANG[k] - PL[ORD[k][0]] + 540) % 360 - 180
def pedido(k):
    th = math.radians(desvio(k)); base = json.load(open(os.path.join(AQUI, 'east-esqueleto', 'pedido.json')))
    I = [LS[0] - 0.19 * math.sin(th), LS[1] + 0.19 * math.cos(th), 0.228]
    P = []
    for q, f in zip(base['poses'], K):
        q = dict(q); s = desvio(k) / 45
        q['left_hand'] = [round(R0[j] + (I[j] - R0[j]) * f, 3) for j in range(3)]
        q['chest'] = q['chest'] + round(3 * s * f); q['hips'] = q['hips'] + round(1 * s * f)
        q['head'] = [q['head'][0] + round(8 * s), q['head'][1]]
        q['left_elbow'] = [-0.5 * s, 0.2, -1] if s else [-0.2, 0.1, -1]
        P.append(q)
    return dict(character_id=CHAR, mode='skeleton-v3', directions=[ORD[k][0]], frame_count=8, poses=P,
                animation_name=f'Jab vista {k + 1}',
                action_description='boxer throws a quick left jab toward where he is looking, feet planted, right glove at the chin')
def verifica(req, k):
    """o golpe tem de ir para onde ele olha: ângulo da mão no impacto = desvio da vista"""
    h = req['poses'][3]['left_hand']; a = math.degrees(math.atan2(-(h[0] - LS[0]), h[1] - LS[1]))
    return abs(a - desvio(k)) < 3, round(a)
def faz(k):
    req = pedido(k); ok, a = verifica(req, k)
    if not ok: print(f'VERIFICAÇÃO FALHOU na vista {k + 1}: jab a {a}° e devia ser {desvio(k)}°'); return False
    t = mcp('animate_character', req)
    if 'error' in t.lower()[:200]: print('ERRO', t[:300]); return False
    mcp('wait_for_jobs', {'timeout_seconds': 300})
    t = mcp('get_character', {'character_id': CHAR})
    i = t.find(req['animation_name']); m = re.search(ORD[k][0] + r': (https://backblaze\S+\{i\}\.png\S*) \(i=0\.\.(\d+)\)', t[i:])
    if not m: print('AINDA A GERAR', k + 1); return False
    pasta = os.path.join(AQUI, f'{ORD[k][0]}-jab'); os.makedirs(pasta, exist_ok=True)
    for j in range(int(m.group(2)) + 1):
        subprocess.run(['curl', '-sS', '-o', os.path.join(pasta, f'{j}.png'), m.group(1).replace('{i}', str(j))], check=True)
    json.dump(req, open(os.path.join(pasta, 'pedido.json'), 'w'))
    e = json.load(open(EST)) if os.path.exists(EST) else {}
    e[str(k)] = ORD[k][0] + '-jab'; json.dump(e, open(EST, 'w'), indent=1)
    print(f'FEITA vista {ORD[k][1]} (jab a {a}°)'); return True
def atlas():
    """8 linhas (uma por vista) x 8 fotogramas de 64x60, alinhados à guarda pelos pés"""
    e = json.load(open(EST)) if os.path.exists(EST) else {}
    out = Image.new('RGBA', (64 * 8, 60 * 8)); P = 12
    for kk, pasta in e.items():
        k = int(kk); n = ORD[k][0]; pasta = os.path.join(AQUI, pasta)
        base = np.array(Image.open(os.path.join(CAB, 'variantes', '00-corpo-base', n + '.png')).convert('RGBA')).astype(int)
        f0 = np.array(Image.open(os.path.join(pasta, '0.png')).convert('RGBA')).astype(int)
        _, ox, oy = min((np.abs(f0[y:y + 60, x:x + 40] - base).sum(), x, y) for y in range(0, f0.shape[0] - 59) for x in range(0, f0.shape[1] - 39))
        y0 = np.nonzero(f0[:, :, 3])[0].max()
        for j in range(8):
            f = Image.open(os.path.join(pasta, f'{j}.png')).convert('RGBA'); dy = np.nonzero(np.array(f)[:, :, 3])[0].max() - y0
            c = f.crop((ox - P, oy + dy, ox + 40 + P, oy + dy + 60))
            if pasta.endswith('east-esqueleto') and j:          # vista 4 antiga: a bota de trás levantava (botas da guarda)
                c0 = Image.open(os.path.join(pasta, '0.png')).convert('RGBA').crop((ox - P, oy + 50, ox + 40 + P, oy + 60))
                c.paste(Image.new('RGBA', (64, 10)), (0, 50)); c.alpha_composite(c0, (0, 50))
            out.paste(c, (j * 64, k * 60))
    out.save(ATLAS); json.dump(sorted(int(k) for k in e), open(LISTA, 'w'))
    print('atlas com as vistas', [ORD[int(k)][1] for k in sorted(e, key=int)])
if __name__ == '__main__':
    e = json.load(open(EST)) if os.path.exists(EST) else {}
    feitas = 0
    for k in ORDEM:
        if str(k) in e and k != 3: continue
        if k == 3 and e.get('3') == 'east-jab': continue
        if gerações() < 3: print('SEM GERACOES para a vista', ORD[k][1]); break
        if faz(k): feitas += 1
        else: break
    atlas()
    falta = [ORD[k][1] for k in ORDEM if not (str(k) in e and (k != 3 or e.get('3') == 'east-jab'))]
    e = json.load(open(EST)); falta = [ORD[k][1] for k in ORDEM if not (str(k) in e and (k != 3 or e['3'] == 'east-jab'))]
    print('feitas hoje:', feitas, '| faltam:', falta or 'NENHUMA')
