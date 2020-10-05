t = int(input())
for _ in range(t):
    n = int(input())
    s = str(input())
    ans = 1
    for i in range(n-1):
        if(s[i+1]!=s[i]):
            ans = ans + 1
    print(ans)