import sys
from PIL import Image
S='/tmp/claude-0/-home-user-Corner-Men/d38ab75d-3fb7-5fe2-9b4c-05387542f032/scratchpad/jab/'
for pasta in sys.argv[1:]:
    fs=[Image.open(f'{pasta}/{i}.png').convert('RGBA') for i in range(8)]
    w,h=fs[0].size; Z=4
    o=Image.new('RGBA',(w*Z*8,h*Z),(60,60,70,255))
    for i,f in enumerate(fs): o.alpha_composite(f.resize((w*Z,h*Z),Image.NEAREST),(i*w*Z,0))
    o.save(S+pasta+'.png')
    fr=[]
    for f in fs:
        b=Image.new('RGBA',(w*6,h*6),(60,60,70,255)); b.alpha_composite(f.resize((w*6,h*6),Image.NEAREST)); fr.append(b.convert('RGB'))
    fr[0].save(S+pasta+'.gif',save_all=True,append_images=fr[1:],duration=[80,50,50,60,130,70,80,80],loop=0)
