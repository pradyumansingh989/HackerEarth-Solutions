n=int(input())
 
a=list(map(int,input().split()))
 
b=list(map(int,input().split()))
 
k=min(a)
 
count=0
 
flag=True
 
for i in range(n):
 
    while(a[i]>k and b[i]!=0):
 
        a[i]=a[i]-b[i]
 
        count=count+1
 
    if(a[i]<0):
 
        flag=False
 
    else:
 
        k=a[i]
 
for i in a:
 
    if(i!=min(a)):
 
        flag=False
 
if(flag==False):
 
    print("-1")
 
else:
 
    print(count)