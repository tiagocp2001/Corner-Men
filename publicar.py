"""Prepara uma nova versão do Corner Men para publicar.

Uso: python3 publicar.py

- sobe a VERSION do sw.js (os telemóveis percebem que há versão nova);
- atualiza a etiqueta no fundo do ecrã do index.html ("vN · dia mês ano");
- confirma que a chave do jogo guardado (KEY) não mudou.

Depois: commit e push para o branch `main` (o GitHub Pages republica em 1–2 minutos).
A fonte do jogo é o próprio index.html do repositório.
"""
import re, sys, datetime

KEY_ESPERADA = 'corner-men-v6'  # mudar só de propósito: apaga o progresso de todos os jogadores

html = open('index.html', encoding='utf8').read()
sw = open('sw.js', encoding='utf8').read()

key = re.findall(r"const KEY='([^']*)'", html)
if key != [KEY_ESPERADA]:
    sys.exit(f'PARAR: a chave do jogo guardado mudou ({key}); esperado {KEY_ESPERADA!r}. Confirmar com o Tiago.')

m = re.findall(r"VERSION = 'v(\d+)'", sw)
if len(m) != 1:
    sys.exit('PARAR: não encontrei uma única VERSION no sw.js')
v = int(m[0]) + 1

meses = 'jan fev mar abr mai jun jul ago set out nov dez'.split()
d = datetime.datetime.now(datetime.timezone.utc)
label = f'v{v} · {d.day:02d} {meses[d.month - 1]} {d.year}'

html2, n = re.subn(r'(<div id="cm-ver"[^>]*>)[^<]*(</div>)', lambda x: x.group(1) + label + x.group(2), html)
if n != 1:
    sys.exit('PARAR: não encontrei a etiqueta de versão (div#cm-ver) no index.html')

open('index.html', 'w', encoding='utf8').write(html2)
open('sw.js', 'w', encoding='utf8').write(re.sub(r"VERSION = 'v\d+'", f"VERSION = 'v{v}'", sw))
print('ok', label)
