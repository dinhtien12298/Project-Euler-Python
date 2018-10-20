# # How many circular primes are there below one million?
from itertools import permutations
from math import ceil

list_primes = []

# Tìm tất cả số nguyên tố dưới 1 triệu
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
# Kiểm tra từng hoán vị của từng số có là nguyên tố không
list_remove = []
for currentPrime in list_primes:
    list_check = list(str(currentPrime))
    for index, item in enumerate(list(permutations(list_check))):
        check_number = list(item)
        for index1, item1 in enumerate(check_number):
            if index1 > 0:
                check_number[0] = int(check_number[0]) * 10 + int(item1)
        if check_number[0] not in list_primes:
            list_remove.append(currentPrime)
            break

for remove_number in list_remove:
    list_primes.remove(remove_number)

print(len(list_primes))