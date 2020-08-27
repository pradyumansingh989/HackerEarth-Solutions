n=int(input())
data=[int(x) for x in input().split()]
d=[]
for x in data:
    lastdigit = (repr(x)[-1])
    d.append(lastdigit)
res="".join(d)
res=int(res)
if(res%10==0):
    print("Yes")
else:
    print("No")