# Factorial digit sum

import math

n = math.factorial(100)
sum = 0

digits = list(str(n))
for index, item in enumerate(digits):
    sum += int(item)

print(sum)