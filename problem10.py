# Tổng các số nguyên tố nhỏ hơn 2.000.000

import math

sum = 2
for i in range(3,2000000):
    isPrime = True
    for j in range(3, int(math.sqrt(i))+1,2):
        if i % j == 0:
            isPrime = False
            break
    if isPrime == True:
        sum += i
    print(i)

print(sum)