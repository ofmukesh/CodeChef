t=int(input());

for i in range(t):
    x,y = map(int,input().split());
    
    if x==0 or y==0:
        print("NO");
    elif x==y:
        print("YES")
    else:
        print("NO")
