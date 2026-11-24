import sys
from PIL import Image, ImageDraw, ImageFont
S='/tmp/claude-0/-home-user-Corner-Men/d38ab75d-3fb7-5fe2-9b4c-05387542f032/scratchpad/'
f=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',22)
saida=sys.argv[1]; ps=[(p.split('-')[-1].upper(),p) for p in sys.argv[2:]]
DUR=[90,80,50,60,90,60,70,60]
fr=[]; o2=Image.new('RGB',(8*200,len(ps)*250),(60,60,70)); d2=ImageDraw.Draw(o2)
bb=Image.open(ps[0][1]+'/0.png').getbbox(); cx=(bb[0]+bb[2])//2
for i in range(8):
    o=Image.new('RGB',(len(ps)*260,330),(60,60,70)); d=ImageDraw.Draw(o)
    for c,(t,p) in enumerate(ps):
        im=Image.open(f'{p}/{i}.png').convert('RGBA').crop((cx-34,bb[1]-6,cx+34,bb[1]+72))
        b=Image.new('RGBA',(260,298),(60,60,70,255)); b.alpha_composite(im.resize((260,298),Image.NEAREST)); o.paste(b.convert('RGB'),(c*260,0)); d.text((c*260+8,302),t,fill=(255,220,120),font=f)
        b2=Image.new('RGBA',(200,229),(60,60,70,255)); b2.alpha_composite(im.resize((200,229),Image.NEAREST)); o2.paste(b2.convert('RGB'),(i*200,c*250))
        if i==0: d2.text((6,c*250+4),t,fill=(255,220,120),font=f)
    fr.append(o)
dd=list(DUR); dd[0]+=600
fr[0].save(S+saida+'.gif',save_all=True,append_images=fr[1:],duration=dd,loop=0); o2.save(S+saida+'.png')
