# Summation of primes

# import math

# sum = 2
# for i in range(3, 2000000, 2):
#     isPrime = True
#     print(i)
#     for j in range(2, int(math.sqrt(i))+1):
#         if i % j == 0 and i != j:
#             isPrime = False
#             break
#     if isPrime == True:
#         sum += i

# print(sum)

from math import ceil
list_primes = []
n = 2000000
primes = [True] * n
primes[0] = False
primes[1] = False
roundUp = lambda n, prime: int(ceil(n / prime))
for currentPrime in range(2, n):
    if not primes[currentPrime]:
        continue
    list_primes.append(currentPrime)
    for i in range(2, roundUp(n, currentPrime)):
        primes[i * currentPrime] = False

print(sum(list_primes))