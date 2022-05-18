n = int(input())

i=1;
num=1;
while i <= n :
    j=1;
    col="";
    while j <= i :
        col=col+str(num)
        num=num+1
        j=j+1;
        if j==2:
            main = num
    if i>1:
        num=main
    print(col)
    i=i+1;
    
    
        
        
        
        
        
        
        
        
