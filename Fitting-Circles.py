t =  int(input())
for i in range(t):
    a,b = map(int,input().split())
    if(a >= b):
        print(a//b)
    elif(a<b):
        print(b//a)