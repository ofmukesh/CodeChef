test=int(input());

for case in range(test):
    M,N,K = map(int,input().split());

    if  M-N*K <=0 :
        print("NO");
    else:
        print("YES");
