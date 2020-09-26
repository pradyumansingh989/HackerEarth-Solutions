def rec(a, b, c):
    if(a >= b):
        return ((a-b)//2+(a-b)%2)
    if(b%c==0):
        return (1 + rec(a,b//c,c))
    else:
        x=(b//c+1)*c;
        return ((x-b)//2 + (x-b)%2 + rec(a,x,c))
 
t = int(input())
while(t > 0):
    a, b, c = map(int, input().split())
    print(rec(a, b, c))
    t -= 1