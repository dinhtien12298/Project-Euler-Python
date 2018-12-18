# Amicable numbers

list_amicable_number = []

for n in range(1,10000):
    if n not in list_amicable_number:
        list_divisor_1 = []
        list_divisor_2 = []

        for i in range(1, int(n/2)+1):
            if n % i == 0 and i not in list_divisor_1:
                list_divisor_1.append(int(i))
                if n/i not in list_divisor_1 and i != 1:
                    list_divisor_1.append(int(n/i))

        pair = sum(list_divisor_1)

        if n != pair:
            for j in range(1, pair):
                if pair % j == 0 and j not in list_divisor_2:
                    list_divisor_2.append(int(j))
                    if n/i not in list_divisor_2 and j != 1:
                        list_divisor_2.append(int(pair/j))

        if sum(list_divisor_2) == n:
            list_amicable_number.append(n)
            list_amicable_number.append(pair)

print(sum(list_amicable_number))