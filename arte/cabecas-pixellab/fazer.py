# Faz a próxima cabeça da lista na PixelLab, se houver gerações grátis que cheguem.
# Uso: python3 -I fazer.py   (correr dentro desta pasta)
import json, subprocess, sys, re, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image
AQUI = os.path.dirname(os.path.abspath(__file__))
L = os.path.join(AQUI, 'lista.json')
DIRS = ['south','south-east','east','north-east','north','north-west','west','south-west']

def mcp(tool, args):
    out = subprocess.run([sys.executable, '-I', os.path.join(AQUI, 'mcp.py'), tool, json.dumps(args)],
                         capture_output=True, text=True).stdout
    d = json.loads(out, strict=False)
    return '\n'.join(c.get('text', '') for c in d['result']['content'])

def disponivel():
    t = mcp('get_balance', {})
    rem = float(re.search(r'generations_remaining: ([\d.]+)', t).group(1))
    hoje = re.search(r'generations_today: ([\d.]+)', t)
    return rem + (float(hoje.group(1)) if hoje else 0), t

def baixar(char_id, pasta):
    os.makedirs(pasta, exist_ok=True)
    t = mcp('get_character', {'character_id': char_id})
    for d in DIRS:
        m = re.search(r'  ' + d + r': (https://backblaze\S+rotations\S+)', t)
        if not m: return False
        subprocess.run(['curl', '-sS', '-o', os.path.join(pasta, d + '.png'), m.group(1)], check=True)
    return True

def comparar(pasta, base):
    S = 5; W, H = 40*S, 60*S
    im = Image.new('RGBA', (W*8, H*2+10), (60, 60, 70, 255))
    for k, d in enumerate(DIRS):
        im.alpha_composite(Image.open(os.path.join(base, d + '.png')).convert('RGBA').resize((W, H), Image.NEAREST), (k*W, 0))
        im.alpha_composite(Image.open(os.path.join(pasta, d + '.png')).convert('RGBA').resize((W, H), Image.NEAREST), (k*W, H+10))
    im.save(os.path.join(pasta, 'comparar.png'))

def main():
    lst = json.load(open(L))
    base = os.path.join(AQUI, 'variantes', '00-corpo-base')
    for c in lst['cabecas']:   # uma que ficou a gerar da última vez
        if c['estado'] == 'a gerar':
            pasta = os.path.join(AQUI, 'variantes', f'{c["n"]:02d}')
            if 'status: completed' in mcp('get_character', {'character_id': c['state_id']}) and baixar(c['state_id'], pasta):
                comparar(pasta, base); fim(lst, c, pasta)
    nxt = next((c for c in lst['cabecas'] if c['estado'] == 'por fazer'), None) \
          or next((c for c in lst['cabecas'] if c['estado'] == 'repetir'), None)
    if not nxt: print('TUDO FEITO'); return
    base = os.path.join(AQUI, 'variantes', '00-corpo-base')
    if not os.path.exists(os.path.join(base, 'south.png')): baixar(lst['corpo_base'], base)
    tem, txt = disponivel()
    if tem < 10:
        print(f'SEM GERACOES: {tem} (precisa de 10). Próxima: {nxt["n"]}'); return
    pedido = lst['modelo_pedido'].replace('{en}', nxt['en'])
    t = mcp('create_character_state', {'character_id': lst['corpo_base'], 'edit_description': pedido,
                                        'state_name': f'Cabeca {nxt["n"]:02d}'})
    sid = re.search(r'id: ([0-9a-f-]{36})', t).group(1)
    nxt['state_id'] = sid; nxt['estado'] = 'a gerar'
    json.dump(lst, open(L, 'w'), ensure_ascii=False, indent=1)
    for _ in range(4):
        mcp('wait_for_jobs', {'timeout_seconds': 300})
        if 'status: completed' in mcp('get_character', {'character_id': sid}): break
    pasta = os.path.join(AQUI, 'variantes', f'{nxt["n"]:02d}')
    if not baixar(sid, pasta):
        print(f'AINDA A GERAR: {nxt["n"]} ({sid})'); return
    comparar(pasta, base)
    fim(lst, nxt, pasta)

def fim(lst, c, pasta):
    """Verifica o corpo píxel a píxel; se mudou, a cabeça fica para repetir."""
    import verificar
    r = verificar.verificar(pasta)
    maus = [f'{d} {p:.1f}%' for d, p in r if p > verificar.LIMITE]
    if maus:
        c['estado'] = 'repetir'; c['porque'] = 'corpo diferente: ' + ', '.join(maus)
    else:
        c['estado'] = 'feita'; c.pop('porque', None)
    json.dump(lst, open(L, 'w'), ensure_ascii=False, indent=1)
    feitas = sum(1 for x in lst['cabecas'] if x['estado'] == 'feita')
    print(('REPETIR' if maus else 'FEITA') + f': {c["n"]} — {c["pt"]}' + (f' ({c["porque"]})' if maus else '') + f' | total feitas: {feitas}/40')

if __name__ == '__main__':
    main()
