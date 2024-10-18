n = int(input())
m = int(input())
a = int(input())

pave_n = (n + a - 1) // a  
pave_m = (m + a - 1) // a  

total_pave = pave_n * pave_m

print(total_pave)
