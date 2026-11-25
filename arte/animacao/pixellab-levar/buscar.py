# Descarrega versões já pedidas à PixelLab (quando a descarga falhou). Uso: buscar.py <jab|direto> <vista> <versões...>
import os, re, subprocess, sys, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'pixellab-jab'))
import jab_vistas as J
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import levar as L
g, k, nomes = sys.argv[1], int(sys.argv[2]) - 1, sys.argv[3:]
d = J.ORD[k][0]
for _ in range(6):
    J.mcp('wait_for_jobs', {'timeout_seconds': 300}); t = J.mcp('get_character', {'character_id': J.CHAR})
    ms = {n: re.search(d + r': (https://backblaze\S+\{i\}\.png\S*) \(i=0\.\.(\d+)\)', t[t.find(f'Levar {g} vista {k + 1} {n}'):]) for n in nomes}
    if all(ms.values()): break
for n, m in ms.items():
    pasta = os.path.join(L.AQUI, f'{d}-{g}-{n}'); os.makedirs(pasta, exist_ok=True)
    for j in range(int(m.group(2)) + 1): subprocess.run(['curl', '-sS', '--retry', '5', '--retry-all-errors', '-o', os.path.join(pasta, f'{j}.png'), m.group(1).replace('{i}', str(j))], check=True)
    print('feita', pasta)
