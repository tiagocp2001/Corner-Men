# cliente MCP mínimo (HTTP + SSE) — a chave é posta pelo proxy
import json, sys, urllib.request
URL = 'https://api.pixellab.ai/mcp'
SID = {}
def call(method, params=None, id_=1):
    body = {"jsonrpc": "2.0", "id": id_, "method": method}
    if params is not None: body["params"] = params
    h = {"Content-Type": "application/json", "Accept": "application/json, text/event-stream"}
    if SID.get('s'): h['Mcp-Session-Id'] = SID['s']
    req = urllib.request.Request(URL, data=json.dumps(body).encode(), headers=h)
    with urllib.request.urlopen(req, timeout=300) as r:
        s = r.headers.get('Mcp-Session-Id')
        if s: SID['s'] = s
        txt = r.read().decode()
    out = None
    for line in txt.splitlines():
        if line.startswith('data:'): out = json.loads(line[5:])
    if out is None and txt.strip(): out = json.loads(txt)
    return out
def init():
    r = call('initialize', {"protocolVersion": "2025-03-26", "capabilities": {}, "clientInfo": {"name": "cliente", "version": "1.0"}})
    try: call('notifications/initialized', {}, id_=None)
    except Exception: pass
    return r
def tool(name, args):
    r = call('tools/call', {"name": name, "arguments": args}, id_=2)
    return r
if __name__ == '__main__':
    init()
    if sys.argv[1] == 'list':
        r = call('tools/list', {}, id_=2)
        for t in r['result']['tools']: print(t['name'], '|', t.get('description', '')[:150].replace('\n', ' '))
    else:
        r = tool(sys.argv[1], json.loads(sys.argv[2]) if len(sys.argv) > 2 else {})
        print(json.dumps(r, ensure_ascii=False)[:6000])
