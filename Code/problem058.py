# Spiral primes

from math import ceil

# Tìm tất cả số nguyên tố dưới 1 triệu
list_all_primes = []
n = 1000000000
primes = [True] * n
primes[0] = False
primes[1] = False
roundUp = lambda n, prime: int(ceil(n / prime))
for currentPrime in range(2, n):
    if not primes[currentPrime]:
        continue
    list_all_primes.append(currentPrime)
    for i in range(2, roundUp(n, currentPrime)):
        primes[i * currentPrime] = False

# Xét
side = 3
loop = True
value = 1
list_number = [1]
list_prime = []

while loop:
    side_run = side - 1
    for i in range(4):
        for k in range(side_run):
            value += 1
        list_number.append(value)
        if value in list_all_primes:
            list_prime.append(value)
    if (float(len(list_prime))/len(list_number)) <= 0.1:
        print(side)
        break
    side += 2