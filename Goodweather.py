test=int(input());

for case in range(test):
   arr = input().split();
   
   r=0;
   s=0;
   for i in range(7):
        if arr[i] == "0":
            r=r+1;
        else:
            s=s+1;
        if r==4:
            print("NO")
            break;
        if s==4:
            print("YES")
            break;
