t=int(input())
for i in range(t):
    x,y,k=map(int,input().split())
    
    total = x*y;
    
    if total>k:
        print("NO");
    else :
        print("YES")
