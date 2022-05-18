t=int(input())

def check(x,y,z):
   
    if x <= y+z :
        print("NO")
    else:
        print("YES")

for i in range(t):
    a,b,c=map(int,input().split());
    
    maxc=max(a,b,c)
    
    if maxc==a:
        check(a,b,c)
    elif maxc==b:
        check(b,a,c)
    elif maxc==c:
        check(c,a,b)
