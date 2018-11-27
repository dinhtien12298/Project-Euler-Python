# Circular primes

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
# Ta được list_primes là list các số nguyên tố dưới 1 triệu

# Tìm số nguyên tố bằng tổng nhiều số nguyên tố nhất
# list_length: List số các số nguyên tố mà 1 số nguyên tố có thể phân tích ra
# list_dictionary: List các bộ giá trị, key là số nguyên tố có thể phân tích được, value là số các số nguyên tố mà key đó có thể phân tích ra
list_length = []
list_dictionary = []
for number in list_primes:
    # list_check: List các số nguyên tố mà 1 số có thể phân tích ra
    list_check = []
    number_real = number
    for i in list_primes:
        if i <= number:
            number -= i
            list_check.append(i)
        elif i > number:
            for j in list_primes:
                if j < i - number:
                    number += j
                    list_check.remove(j)
                elif j == i - number:
                    number = 0
                    list_check.append(i)
                    list_check.remove(j)
                    break
                elif j > i - number:
                    break
            break
        if number == 0:
            break
    if number == 0:
        list_length.append(len(list_check))
        list_dictionary.append({number_real:len(list_check)})

# Duyệt từng bộ giá trị trong list_dictionary, đến key có value bằng với giá trị lớn nhất trong list_length thì dừng lại và key là số nguyên tố cần tìm
loop = True
for index, item in enumerate(list_dictionary):
    if loop == True:
        for key, value in item.items():
            if value == max(list_length):
                print(key)
                loop = False
                break
    elif loop == False:
        break