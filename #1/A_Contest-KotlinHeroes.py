# t = int(input()) # to take tests t times from input

# results = [] # this empty list is for storing results and showing input at the end


# for _ in range(t):   # for t times looping to get result
#     x, y = map(int, input().split()) # getting values from console
    
#     results.append((min(x, y), max(x, y))) #adding our values(finding max&min with python's math function) to list 
    
# for result in results: #looping for result item inside of results

#      print(result[0], result[1]) #showing sorted input values by selecting list[index]

t = int(input())

for _ in range(t):
    x,y = map(int, input().split())
    
    if x>y :
       print(y, " ", x) 
    # min to max
    elif x<=y :
        print(x, " ",y)
    