# Triangular, pentagonal, and hexagonal

def is_pentagonal(n):
    if (1+(24*n+1)**0.5) % 6 == 0:
        return True
    return False

def is_hexagonal(n):
    if (1+(8*n+1)**0.5) % 4 == 0:
        return True
    return False

loop = True
i = 286
while loop:
    a = i*(i+1)/2
    if is_pentagonal(a) and is_hexagonal(a):
        print(a)
        loop = False
        break
    i += 1