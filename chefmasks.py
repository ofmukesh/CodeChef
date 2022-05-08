t=int(input());

for i in range(t):
    x,y = map(int,input().split());
    
    c = y*10;
    d = x*100;
    
    if c==d or c<d:
        print("Cloth");
    else:
        print("Disposable");
