"""Turns the Claude artifact's index.html into the Corner Men web app.
Usage: python3 build.py <artifact index.html>   (writes ./index.html, bumps sw.js version)"""
import sys, re
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
open('index.html', 'w', encoding='utf8').write(s)
sw = open('sw.js').read()
v = int(re.search(r"VERSION = 'v(\d+)'", sw).group(1)) + 1
open('sw.js', 'w').write(re.sub(r"VERSION = 'v\d+'", f"VERSION = 'v{v}'", sw))
print('ok, sw', v)
