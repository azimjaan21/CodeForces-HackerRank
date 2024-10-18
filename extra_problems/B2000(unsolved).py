t = int(input())  

for _ in range(t):
    n = int(input())  
    seats = list(map(int, input().split()))  
    seats.sort()

    valid = True  
    for i in range(1, n):
        if seats[i] - seats[i - 1] != 1:  
            valid = False
            break

    if valid:
        print("YES")
    else:
        print("NO")