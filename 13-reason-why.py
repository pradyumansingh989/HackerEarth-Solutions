A,B,C = input().split()
A = int(A)
B = int(B)
C = int(C)
# swapping
# temp=A
# A=B
# B=temp
A,B=B,A
# operations
A = A * C
B = C + B
 
print(A,B)