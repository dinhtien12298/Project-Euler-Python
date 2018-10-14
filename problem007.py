# Số nguyên tố thứ 10001

list_prime = []
number = 2

while len(list_prime) <= 10001:
    list_un_prime = []
    for j in range(2,number//2):
        if number % j == 0:
            list_un_prime.append(j)
            break
    if len(list_un_prime) == 0:
        list_prime.append(number)
    number += 1

print(list_prime[-1])