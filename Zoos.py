word = input()
 
from collections import Counter
x = Counter(word)
if(x['z']*2 == x['o']):
    print('Yes')
else:
    print('No')