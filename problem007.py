# 10001st prime

# list_prime = []
# number = 2

# while len(list_prime) <= 10001:
#     list_un_prime = []
#     for j in range(2,number//2):
#         if number % j == 0:
#             list_un_prime.append(j)
#             break
#     if len(list_un_prime) == 0:
#         list_prime.append(number)
#     number += 1

# print(list_prime[-1])

from math import ceil
list_primes = []
n = 1000000
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
    if len(list_primes) == 10001:
        break

print(list_primes[-1])