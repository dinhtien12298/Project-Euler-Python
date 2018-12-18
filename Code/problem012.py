# Highly divisible triangular number
import math

def number_of_divisor(n): 
    nod = 0
    for i in range(1, math.ceil(math.sqrt(n))):
        if n % i == 0:
            nod += 2
        elif i ** 2 == n:
            nod -= 1
    return nod

i = 1
while True:
    tn = (i * (i + 1) / 2) # tn: triangle number
    if number_of_divisor(tn) > 500:
        print(tn)
        break
    i += 1