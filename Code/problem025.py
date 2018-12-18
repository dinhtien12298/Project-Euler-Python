# 1000-digit Fibonacci number

fibonacci = [1,1]

loop = True
while loop:
    number = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(number)
    if number >= 10 ** 999:
        loop = False

print(len(fibonacci))