t=int(input())

for i in range(t):
    n,x,p=map(int,input().split());
    
    not_ans = n-x;
    marks = (x*3)+(not_ans*(-1))
    if marks < p :
        print("FAIL")
    else:
        print("PASS")
