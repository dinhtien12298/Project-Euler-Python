list_result = []

for a in range(10,100):
    for b in range(10,100):
        if a != b and a % 10 != 0 and b % 10 != 0 and a/b < 1:
            list_a = list(str(a))
            list_b = list(str(b))
            for digit in list_a:
                if digit in list_b:
                    list_a.remove(digit)
                    list_b.remove(digit)
                    if int(list_b[0]) != 0 and a/b == int(list_a[0]) / int(list_b[0]):
                        list_result.append([int(list_a[0]), int(list_b[0])])

product = 1
for i in range(4):
    product *= list_result[i][1]
    product /= list_result[i][0]

print(product)