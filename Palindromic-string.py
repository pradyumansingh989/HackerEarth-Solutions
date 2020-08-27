s = input()
def palindrome(s):
    return s == s[::-1]
 
ans = palindrome(s)
 
if(ans):
    print("YES")
else:
    print("NO")