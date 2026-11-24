# Guarda a saltitar pelo modo de texto (v3) da PixelLab: sem esqueleto, para ela poder pôr o boneco em bicos dos pés.
import json, os, re, subprocess, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, '..', 'pixellab-jab'))
import jab_vistas as J
DESC = ('boxer in guard bouncing lightly on the balls of his feet, heels lifted off the ground, '
        'weight shifting from one foot to the other with each small bounce, gloves stay up in guard, no punches, '
        'stays in place facing the same way')
for d in ['east', 'south']:
    t = J.mcp('animate_character', dict(character_id=J.CHAR, mode='v3', directions=[d], frame_count=8,
                                        animation_name='Guarda texto ' + d, action_description=DESC))
    print(d, [l for l in t.splitlines() if l.startswith('cost')])
for _ in range(3): J.mcp('wait_for_jobs', {'timeout_seconds': 300})
t = J.mcp('get_character', {'character_id': J.CHAR})
for d in ['east', 'south']:
    i = t.find('Guarda texto ' + d); m = re.search(d + r': (https://backblaze\S+\{i\}\.png\S*) \(i=0\.\.(\d+)\)', t[i:])
    pasta = os.path.join(AQUI, 'texto-' + d); os.makedirs(pasta, exist_ok=True)
    for j in range(int(m.group(2)) + 1): subprocess.run(['curl', '-sS', '-o', os.path.join(pasta, f'{j}.png'), m.group(1).replace('{i}', str(j))], check=True)
    print('feito', d, int(m.group(2)) + 1, 'fotogramas')
