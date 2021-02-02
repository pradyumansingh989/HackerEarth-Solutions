for _ in range(int(input())):
    a=input()
    b=[0,0,0,0,0]
    for i in a:
        if i=="a" or i=="A":
            b[0]=1
        elif i=="e" or i=="E":   
            b[1]=1
        elif i=="i" or i=="I":
            b[2]=1
        elif i=="o" or i=="O":
            b[3]=1
        elif i=="u" or i=="U":      
            b[4]=1
    if b[0]==1 and b[1]==1 and b[2]==1 and b[3]==1 and b[4]==1:
        print("lovely string")
    else:
        print("ugly string")
