for _ in range(int(input())):
    x=list(input())
    if x[::]==x[::-1]:
       print(-1)
    else:
        print(''.join(sorted(x)))