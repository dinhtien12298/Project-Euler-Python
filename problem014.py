# Which starting number, under one million, produces the longest chain?

list_longest = []

number = 2
while number < 1000000:
    list_check = [number]
    number_check = number
    while number_check != 1:
        if number_check % 2 == 0:
            number_check = number_check / 2
            list_check.append(number_check)
        elif number_check % 2 == 1:
            number_check = number_check * 3 + 1
            list_check.append(number_check)
    if len(list_check) > len(list_longest):
        list_longest = list_check

    number += 1

print(list_longest[0])