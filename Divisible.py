n = int(input())
a = map(str,input().split())
d = n/2
res = " "
count = 0 
for i in a:
    count = count + 1
    if(count<=d):
        res = res + i[0]
    else:
        res = res + i[-1]
res = int(res)
if(res % 11 == 0):
    print("OUI")
else:
    print("NON")