d = {'0' : 6, '1' : 2, '2' : 5, '3' : 5, '4' : 4,'5' : 5, '6' : 6, '7' : 3, '8' : 7, '9' : 6}


for _ in range(int(input())):
    stick = 0
    for ch in input():
        stick += d[ch]
        one = stick // 2
        if stick % 2:
            ans = '7' + '1'*(one-1)
        else:
            ans = '1'*one
    print(ans)