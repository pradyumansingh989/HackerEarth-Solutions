x,y,z=input().split()
x=int(x)
y=int(y)
z=int(z)
if(x>y and x>z):
    print(x)
elif(y>x and y>z):
    print(y)
else:
    print(z)