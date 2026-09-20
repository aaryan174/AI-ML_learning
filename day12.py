win=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
p=a=0

def result(b):
    for x,y,z in win:
        if b[x]!=" " and b[x]==b[y]==b[z]: return b[x]
    return "D" if " " not in b else None

def mini(b,maxi):
    global p
    p+=1
    r=result(b)
    if r: return {"X":1,"O":-1,"D":0}[r]
    s=-9 if maxi else 9
    for i in range(9):
        if b[i]==" ":
            b[i]="X" if maxi else "O"
            v=mini(b,not maxi); b[i]=" "
            s=max(s,v) if maxi else min(s,v)
    return s

def ab(b,maxi,al=-9,be=9):
    global a
    a+=1
    r=result(b)
    if r: return {"X":1,"O":-1,"D":0}[r]
    s=-9 if maxi else 9
    for i in range(9):
        if b[i]==" ":
            b[i]="X" if maxi else "O"
            v=ab(b,not maxi,al,be); b[i]=" "
            s=max(s,v) if maxi else min(s,v)
            if maxi: al=max(al,s)
            else: be=min(be,s)
            if be<=al: break
    return s

b=["X","O"," "," "," "," "," "," "," "]

def best(f):
    global p,a
    n=0; score=-9
    for i in range(9):
        if b[i]==" ":
            b[i]="X"; v=f(b,False); b[i]=" "
            if v>score: score,n=v,i
    return n,score

p=0; m=best(mini)
a=0; q=best(ab)

print("Minimax:",m,"States:",p)
print("Alpha-Beta:",q,"States:",a)