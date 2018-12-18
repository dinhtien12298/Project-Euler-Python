# Even Fibonacci numbers

fibonacci = [1,2]
total = []

for i in range(4000001):
    if i == fibonacci[-1] + fibonacci[-2]:
        fibonacci.append(i)

for j in fibonacci:
    if j % 2 ==0:
        total.append(j)

print(sum(total))