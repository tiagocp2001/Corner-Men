"""Turns the Claude artifact's index.html into the Corner Men web app.
Usage: python3 build.py <artifact index.html>   (writes ./index.html, bumps sw.js version)"""
import sys, re, datetime
src = open(sys.argv[1], encoding='utf8').read()
head = '''<meta charset="utf-8">
<link rel="manifest" href="manifest.json">
<meta name="theme-color" content="#17130f">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Corner Men">
<link rel="apple-touch-icon" href="icons/icon-180.png">
<link rel="icon" type="image/png" href="icons/icon-192.png">'''
s = src.replace('<meta charset=utf8>', head, 1)
s = re.sub(r'<title>[^<]*</title>', '<title>Corner Men</title>', s, count=1)
s = s.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', '')
s = s.replace('padding-bottom:env(safe-area-inset-bottom,0px)}', 'padding-bottom:0}', 1)
reg = "<script>\nif('serviceWorker' in navigator){addEventListener('load',()=>navigator.serviceWorker.register('sw.js').catch(()=>{}))}\n</script>\n"
i = s.rfind('</body>'); s = s[:i] + reg + s[i:]
for need in ('rel="manifest"', '<title>Corner Men</title>', "register('sw.js')", 'padding-bottom:0}'):
    assert need in s, 'falta: ' + need
sw = open('sw.js').read()
v = int(re.search(r"VERSION = 'v(\d+)'", sw).group(1)) + 1
open('sw.js', 'w').write(re.sub(r"VERSION = 'v\d+'", f"VERSION = 'v{v}'", sw))
meses = 'jan fev mar abr mai jun jul ago set out nov dez'.split()
d = datetime.datetime.now(datetime.timezone.utc)
label = f"v{v} · {d.day:02d} {meses[d.month-1]} {d.year}"
tag = ('<div id="cm-ver" style="position:fixed;left:0;right:0;bottom:max(0px,calc(env(safe-area-inset-bottom,0px) - 16px));'
       'text-align:center;font:8px/8px \'Press Start 2P\',monospace;color:#a8957d;opacity:.7;pointer-events:none;z-index:40">'
       + label + '</div>\n')
i = s.rfind('<script>\nif(\'serviceWorker\''); s = s[:i] + tag + s[i:]
open('index.html', 'w', encoding='utf8').write(s)
print('ok', label)
