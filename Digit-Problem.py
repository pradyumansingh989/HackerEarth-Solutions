x,k = map(int,input().split())
x = list(str(x))
for i in range(len(x)):
    if(k != 0):
        if(x[i] != '9'):
            x[i] = '9'
            k = k - 1
        else:
            continue
print(''.join(x))