# Quadratic primes

from math import sqrt

v_a = 0
v_b = 0
nop = 0

def isPrime(n):
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

for a in range(-1000, 1001):
    for b in range(-1000, 1001):
        n = 0
        while ((n ** 2 + a * n + b) > 0) and isPrime(n ** 2 + a * n + b):
            n += 1
        if n > nop:
            nop = n
            v_a = a
            v_b = b

print(v_a, v_b)
print(v_a*v_b)