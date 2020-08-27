NumberOfTestCases = int(raw_input())
SeatNumber = list()
rem = 0
while NumberOfTestCases:
    SeatNumber.append(int(raw_input()))
    NumberOfTestCases -=1
 
for i in range(len(SeatNumber)):
    rem = SeatNumber[i]%12
    if rem == 1: #Window Seat
        print '{0} {1}'.format(SeatNumber[i]+11,'WS')
    elif rem == 2: #Middle Seat
        print '{0} {1}'.format(SeatNumber[i]+9,'MS')
    elif rem == 3: #Aisle Seat
        print '{0} {1}'.format(SeatNumber[i]+7,'AS')
    elif rem == 4: #Aisle Seat
        print '{0} {1}'.format(SeatNumber[i]+5,'AS')
    elif rem == 5: #Middle Seat
        print '{0} {1}'.format(SeatNumber[i]+3,'MS')
    elif rem == 6: #Window Seat
        print '{0} {1}'.format(SeatNumber[i]+1,'WS')
    elif rem == 7: #Window Seat
        print '{0} {1}'.format(SeatNumber[i]-1,'WS')
    elif rem == 8: # Middle Seat
        print '{0} {1}'.format(SeatNumber[i]-3,'MS')
    elif rem == 9: #Aisle Seat
        print '{0} {1}'.format(SeatNumber[i]-5,'AS')
    elif rem == 10: #Aisle Seat
        print '{0} {1}'.format(SeatNumber[i]-7,'AS')
    elif rem == 11: #Middle Seat
        print '{0} {1}'.format(SeatNumber[i]-9,'MS')
    elif rem == 0: #Window Seat
        print '{0} {1}'.format(SeatNumber[i]-11,'WS')
   
    rem = 0