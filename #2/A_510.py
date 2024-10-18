print('First number should be odd number (TOQ SON):')
m, n = map(int, input().split())  # Inputing numbers for m & n
 #  ___ m<= 50 ____ n >= 3  * n is odd number* ___

i = 0 #we have to calculate loop for each row
for _ in range(m): # m = Rows (line numbers)
    
    if i%2 == 1: # if i is odd, we put 2nd if operators
        i+=1 # we increase i tto 1 each time
        if i%2 == 0 and i%4 == 0: # checking for i%4 = 0
            print('#' + (n-1)*'.') # print #....(n times)
        else:
            print('.'*(n-1) + '#') #print n(times)....#
    elif i%2 ==0: #it is our odd lines, but even i (0,2,4,...)
        i+=1    #increasing by 1 when every loop works
        print(n*'#')  # print ########## (n times)
    

