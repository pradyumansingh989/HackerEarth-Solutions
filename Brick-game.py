n=int(input())
count=0
for i in range(n):
    count += i
    if(count>=n):
        print("Patlu")
        exit()
    count += 2*i
    if(count>=n):
        print("Motu")
        exit()