for i in range(int(input())):
    a,b=input(),''
    b+=a[0].lower()
    for j in range(1,len(a)):
        if(a[j].isupper()==True):
            b=b+'_'+a[j].lower()
        elif(a[j].islower()==True):
            b+=a[j]
    print(b)