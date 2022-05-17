t=int(input())

for i in range(t):
    w,x,y,z=map(int,input().split());
    
    if x > w+(y*z):
        print("Unfilled");
    elif x < w+(y*z):
        print("overFlow");
    elif x==w+(y*z):
        print("filled");
