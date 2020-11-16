n=int(input())
 
l=list(map(int,input().split()))
 
c=0
 
s=0
 
for i in range(n):
    c=0
 
    for j in l:
        if str(i) in list(str(j)):
            c+=1
            s=max(s,c)
print(s)