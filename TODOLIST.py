t=int(input())

for i in range(t):
    l=input();
    arr=input().split();
    
    count=0;
    
    for j in range(int(l)):
        if int(arr[j])>=1000:
            count=count+1;
            
    print(count)
