t=int(input())

for i in range(t):
    x,m,d = map(int,input().split())
    
    f = x*m
    s = x+d
    
    if f>s:
        print(s)
    else:
        print(f)
