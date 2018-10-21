# Self powers

sum = 0

for i in range(1,1001):
    sum += i**i

print(''.join(list(str(sum))[-10:-1])+list(str(sum))[-1])