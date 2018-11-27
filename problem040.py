# Champernowne's constant

sequence = " "

loop = True
i = 1
while loop:
    sequence += str(i)
    i += 1
    list_check = list(sequence)
    if len(list_check) >= 1000001:
        break

value = int(list_check[1]) * int(list_check[100]) * int(list_check[1000]) * int(list_check[10000]) * int(list_check[100000]) * int(list_check[1000000])

print(value)