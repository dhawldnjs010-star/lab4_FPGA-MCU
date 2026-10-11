import re, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Polygon
plt.rcParams['font.family']='Noto Sans CJK KR'; plt.rcParams['font.size']=6.5
plt.rcParams['axes.unicode_minus']=False
INK='#1f2933'; BLUE='#1f5f99'; GREY='#8b95a1'; LIGHT='#e8edf2'; ORG='#c2410c'
W=8.4/2.54  # inch (column width)

def parse_vcd(path):
    ids={}; sig={}; t=0; cur=None; scope=[]
    for line in open(path):
        line=line.strip()
        m=re.match(r'\$var \w+ (\d+) (\S+) (\S+)',line)
        if m: ids[m.group(2)]=m.group(3); sig[m.group(3)]=[]; continue
        if line.startswith('#'): t=int(line[1:]); continue
        m=re.match(r'b([01xz]+) (\S+)$',line)
        if m and m.group(2) in ids:
            v=m.group(1); sig[ids[m.group(2)]].append((t,int(v,2) if set(v)<=set('01') else None)); continue
        m=re.match(r'([01xz])(\S+)$',line)
        if m and m.group(2) in ids and not line.startswith('$'):
            sig[ids[m.group(2)]].append((t,int(m.group(1)) if m.group(1) in '01' else None))
    return sig
def val_at(ev,t):
    v=None
    for tt,x in ev:
        if tt<=t: v=x
        else: break
    return v

def bus_row(ax,y,ev,t0,t1,step,label,h=0.6):
    # draw bus segments: value changes only at sample points
    pts=[(t,val_at(ev,t)) for t in range(t0,t1+1,step)]
    # compress runs
    runs=[]
    for t,v in pts:
        if runs and runs[-1][2]==v: runs[-1][1]=t+step
        else: runs.append([t,t+step,v])
    for a,b,v in runs:
        b=min(b,t1+step)
        ax.add_patch(Polygon([(a+0.08,y),(a+0.25,y+h/2),(b-0.25,y+h/2),(b-0.08,y),(b-0.25,y-h/2),(a+0.25,y-h/2)],closed=True,fc=LIGHT,ec=BLUE,lw=0.7))
        ax.text((a+b)/2,y,'?' if v is None else str(v),ha='center',va='center',color=INK,fontsize=6)
    ax.text(t0-0.5,y,label,ha='right',va='center',color=INK,fontsize=6.5)

def panel(sigs,names,t0,t1,fname,title,unit='ns',bits={}):
    fig,ax=plt.subplots(figsize=(W,0.42*len(names)+0.55),dpi=300)
    ys=list(range(len(names)))[::-1]
    for y,n in zip(ys,names):
        if n in bits:   # 1-bit
            ev=sigs[n]; xs=[];vv=[]
            for t in range(t0,t1+1):
                xs.append(t); vv.append(val_at(ev,t*1000) or 0)
            ax.step(xs,[y-0.25+0.5*v for v in vv],where='post',color=BLUE,lw=1.0)
            ax.text(t0-0.5,y,n,ha='right',va='center',color=INK,fontsize=6.5)
        else:
            evs=[(t//1000,v) for t,v in sigs[n]]
            bus_row(ax,y,evs,t0,t1,1,n)
    ax.set_xlim(t0,t1+1); ax.set_ylim(-0.6,len(names)-0.4)
    ax.set_yticks([]); ax.set_xticks(range(t0,t1+2,2 if t1-t0<=24 else 4))
    ax.tick_params(axis='x',labelsize=6,length=2,colors=INK)
    for s in ('top','right','left'): ax.spines[s].set_visible(False)
    ax.spines['bottom'].set_color(GREY)
    ax.set_xlabel('시간 (ns)',fontsize=6.5,color=INK,labelpad=1)
    fig.subplots_adjust(left=0.13,right=0.99,top=0.97,bottom=0.22)
    fig.savefig(fname); plt.close(fig)

m=parse_vcd('mult.vcd'); b=parse_vcd('bcd.vcd')
# timescale 1ns/1ps -> VCD times in ps (since precision 1ps) ; events at 1000*k
panel(m,['a','b','m'],0,20,'fig/mult_start.png','')
panel(m,['a','b','m'],237,256,'fig/mult_end.png','')
panel(b,['ten','one','bin','valid'],148,164,'fig/bcd_valid.png','',bits={'valid':1})

# --- firmware LED timeline ---
ev=[l.split() for l in open('fw/fw_log.txt')]
tog=[int(t)/1000 for k,t,v in ev if k=='T']
press=[int(t)/1000 for k,t,v in ev if k=='B' and v=='1']
fig,ax=plt.subplots(figsize=(W,1.55),dpi=300)
xs=[0];ys=[0];s=0
for t in tog:
    if t>60: break
    xs+= [t,t]; ys+=[s,1-s]; s=1-s
xs.append(60); ys.append(s)
ax.plot(xs,ys,color=BLUE,lw=1.0)
first=[3,10,22,30,50]
for p in first: ax.axvline(p,color=ORG,lw=0.8,ls=(0,(3,2)))
lab={0:'1 s',3:'2 s',10:'4 s',22:'8 s',30:'1 s',50:'2 s'}
edges=[0]+first+[60]
for i,k in enumerate([0]+first):
    ax.text((edges[i]+edges[i+1])/2,1.28,lab[k],ha='center',va='bottom',fontsize=6,color=INK)
ax.set_xlim(0,60); ax.set_ylim(-0.1,1.1); ax.set_yticks([0,1]); ax.set_yticklabels(['꺼짐','켜짐'],fontsize=6)
ax.set_xticks(range(0,61,10)); ax.tick_params(axis='x',labelsize=6,length=2,pad=2)
for sp in ('top','right'): ax.spines[sp].set_visible(False)
ax.set_xlabel('시간 (s)',fontsize=6.5,labelpad=1)
fig.subplots_adjust(left=0.13,right=0.97,top=0.82,bottom=0.26)
fig.savefig('fig/led_timeline.png'); plt.close(fig)

# --- wiring ---
fig,ax=plt.subplots(figsize=(W,1.25),dpi=300); ax.set_xlim(0,10); ax.set_ylim(0,4); ax.axis('off')
ax.add_patch(plt.Rectangle((0.1,0.6),2.8,2.8,fc=LIGHT,ec=INK,lw=0.8))
ax.text(1.5,3.05,'NUCLEO-G474RE',ha='center',fontsize=6,color=INK)
ax.text(1.5,2.4,'PB0\n(GPIO_OUT1_ece2)',ha='center',va='center',fontsize=6,color=INK)
ax.text(1.5,1.0,'GND',ha='center',va='center',fontsize=6,color=INK)
ax.plot([2.9,3.6],[2.4,2.4],color=INK,lw=1)
ax.add_patch(plt.Rectangle((3.6,2.15),1.6,0.5,fc='white',ec=INK,lw=0.8)); ax.text(4.4,2.4,'330 Ω ~ 1 kΩ',ha='center',va='center',fontsize=5.5,color=INK)
ax.plot([5.2,6.4],[2.4,2.4],color=INK,lw=1)
ax.add_patch(Polygon([(6.4,2.0),(6.4,2.8),(7.3,2.4)],closed=True,fc='white',ec=INK,lw=0.8)); ax.plot([7.3,7.3],[2.0,2.8],color=INK,lw=1)
ax.text(6.85,3.15,'LED',ha='center',fontsize=6,color=INK); ax.text(6.2,1.7,'+ (긴 다리)',ha='center',fontsize=5.5,color=GREY); ax.text(7.7,1.7,'− (짧은 다리)',ha='left',fontsize=5.5,color=GREY)
ax.plot([7.3,8.6,8.6],[2.4,2.4,1.0],color=INK,lw=1); ax.plot([2.9,8.6],[1.0,1.0],color=INK,lw=1)
ax.plot([8.1,9.1],[1.0,1.0],color=INK,lw=1); ax.plot([8.3,8.9],[0.8,0.8],color=INK,lw=1); ax.plot([8.5,8.7],[0.6,0.6],color=INK,lw=1)
fig.subplots_adjust(left=0.01,right=0.99,top=0.99,bottom=0.01); fig.savefig('fig/wiring.png'); plt.close(fig)
print('ok')
