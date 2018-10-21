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

# Kiểm tra tất cả các số nguyên tố có đảo không là số nguyên tố và thêm vào 1 list
list_remove = []
for number_check in list_primes:
    print(len(list_remove))
    if ("2" in str(number_check)) or ("4" in str(number_check)) or ("6" in str(number_check)) or ("8" in str(number_check)) or ("0" in str(number_check)) or ("5" in str(number_check)):
        list_remove.append(number_check)
        continue
    number = str(number_check)
    for i in range(0, len(number)):
        rotatedNumber = number[i:len(number)] + number[0:i]
        if int(rotatedNumber) not in list_primes:
            list_remove.append(number_check)

# Remove tất cả số nguyên tố đảo đi thì không là số nguyên tố ra khỏi list tất cả số nguyên tố
for remove_number in list_remove:
    if remove_number in list_primes:
        list_primes.remove(remove_number)

# Trong quá trình lọc thì lọc cả số 2 và 5 thỏa mãn nên ta thêm lại
list_primes.append(2)
list_primes.append(5)

print(len(list_primes))