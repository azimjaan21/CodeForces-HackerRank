t = int(input()) #inputing t from console

numbers =[]  #to store test cases on list(loop holatida t marta test uchun sikl)

for _ in range(t):
    n = int(input())   # # 78 = xy = {n}
    
    x=n//10 #to find tens_number (o'nlik son)
    y=n%10 #to find ones_number (birlik son)
    
    numbers.append(x + y)  #calculating tens & ones numbers' sum(raqamlar yig'indisi)
    
for number in numbers:
        print(number)