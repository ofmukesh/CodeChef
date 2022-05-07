t = int(input())

for i  in range(t):
    h,x = map(int,input().split())
    
    if h>=x:
        print("YES")
    else:
        print("NO")
