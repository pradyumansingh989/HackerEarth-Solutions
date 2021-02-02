N = int(input())
A = [int(i) for i in input().split()]
k = sum(A)
l = []
for i in A:
    if (k - i) % 7 == 0:
        l.append(i)

if len(l) == 0:
    print(-1)
else:
    print(A.index(min(l)))

