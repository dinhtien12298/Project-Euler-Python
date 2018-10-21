# Combinatoric selections

from math import factorial as f

count = 0

def ncr(n, r):
    return f(n)/(f(r)*f(n-r))

for n in range(23, 101):
    for r in range(1, n):
        if ncr(n, r) > 1000000:
            count += 1

print(count)