str = input()
for i in str:
    if(i!='A' and i!='C' and i!='G' and i!='T'):
        print('Invalid Input')
        exit()
for i in str:
    if(i == 'A'):
        print('U',end='')
    elif(i == 'C'):
        print('G',end='')
    elif(i == 'G'):
        print('C',end='')
    elif(i == 'T'):
        print('A',end='')
