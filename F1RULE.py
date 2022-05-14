t=int(input())
for i in range(t):
    x,y=map(float,input().split())
    
    rule = float((x/100)*7)
    time = x+rule
    
    if y>time:
        print("NO")
    else:
        print("YES")
