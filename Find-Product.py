n = int(input())
ans = 1
arr = [int(i) for i in input().split()]
for i in arr:
    ans = (ans * i)%(pow(10,9)+7)
print(ans)