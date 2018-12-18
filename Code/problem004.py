# Largest palindrome product

def isPalindromic(n):
    if str(n) == str(n)[::-1]: return True
    return False

for i in range(999*999, 10000, -1):
    j = 100
    isFound = False
    while j < 1000 and isPalindromic(i):
        if i % j != 0: j += 1
        else:
            k = i / j
            if 99 < k < 1000:
                print(i)
                isFound = True
                break
            else:
                j += 1
    if isFound:
        break