l,r,k = input().split()
l=int(l)
r=int(r)
k=int(k)
count=0
for i in range(l,r+1):
    if(i%k==0):
        count=count+1
print(count)