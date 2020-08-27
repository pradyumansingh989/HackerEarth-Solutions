l = int(input())
n = int(input())
for i in range(1,n+1):
    w,h = input().split()
    w=int(w)
    h=int(h)
    if(w < l):
        print("UPLOAD ANOTHER")
    elif(h < l):
        print("UPLOAD ANOTHER")
    elif(w==h):
        print("ACCEPTED")
    elif(w==l and h==l):
        print("ACCEPTED")
    else:
        print("CROP IT")