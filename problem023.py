# Non-abundant sums

from math import sqrt

def isAbundant(n):
    list_divisors = []
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            list_divisors.append(i)
            list_divisors.append(n/i)
        if i ** 2 == n:
            list_divisors.remove(i)
    if sum(list_divisors) > n:
        return True
    else:
        return False

list_abundant = []
for i in range(1, 28123):
    if isAbundant(i):
        list_abundant.append(i)

list_sum = [x for x in range(28123)]
for i in range(len(list_abundant)):
    for j in range(i, len(list_abundant)):
        if list_abundant[i] + list_abundant[j] < 28123:
            list_sum[list_abundant[i] + list_abundant[j]] = 0
        
print(sum(list_sum))