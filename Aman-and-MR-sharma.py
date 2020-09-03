days=int(input())
toffee=0
for i in range(days):
    r,x=list(map(int, input().split()))
    run=100*x
    perimeter=2*(22/7)*r
    if(run>=perimeter):
        toffee=toffee+1
print(toffee)