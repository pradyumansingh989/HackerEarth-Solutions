n,q = map(int,input().split())
arr = list(map(int,input().split()))
for i in range(1,len(arr)):
    arr[i] = arr[i] + arr[i-1]
for _ in range(q):
    s,e = map(int,input().split())
    if s==1:
        sum1 = arr[e-1]
        avg = sum1//(e-s+1) #floor division
        print(avg)
    else:
        sum1 = arr[e-1] - arr[s-2]
        avg = sum1//(e-s+1) #floor divison
        print(avg)