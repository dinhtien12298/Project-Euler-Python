# Tổng các số nguyên tố nhỏ hơn 2.000.000

import math

sum = 2
for i in range(3, 2000000, 2):
    isPrime = True
    for j in range(2, int(math.sqrt(i))+1):
        if i % j == 0 and i != j:
            isPrime = False
            break
    if isPrime == True:
        sum += i

print(sum)