n = input()
if(len(n)!= 10):
    print("Illegal ISBN")
else:
    sum = 0
    count=0
    for i in n:
        count += 1
        sum = sum + (int(i)*count)
    if(sum % 11 == 0):
        print("Legal ISBN")
    else:
        print("Illegal ISBN")
        