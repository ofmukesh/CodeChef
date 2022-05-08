t=int(input())

for i in range(t):
    A,B,C = map(int,input().split())
    minum = min(A,B,C)
    
    if A==minum:
        print("Draw")
    elif B==minum:
        print("Bob")
    elif C==minum:
        print("Alice")
