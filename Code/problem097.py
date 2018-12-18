# Large non-Mersenne prime
 
n = 2
for i in range(7830456): n = (2 * n) % 10000000000
 
n = n * 28433 + 1
n = n % 10000000000

print(n)