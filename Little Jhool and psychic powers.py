num = input()
 
for i in range(len(num)):
    if(num[i:i+6] == '000000' or num[i:i+6] == '111111'):
        print('Sorry, sorry!')
        break
    elif(int(i)==len(num)-1):
        print('Good luck!')