# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

sum = 25 # side = 3
last_number = 9

for i in range(3, 1000, 2):
    for j in range(4):
        last_number += i + 1
        sum += last_number
        
print(sum)