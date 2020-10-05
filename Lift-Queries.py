A = 0
B = 7
for _ in range(int(input())):
    n = int(input())
    if(abs(B - n) < abs(n - A)):
        print("B")
        B = n
    elif(abs(B - n) > abs( n- A)):
        print("A")
        A = n
    else:
        print("A")
        A = n