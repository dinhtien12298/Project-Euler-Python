# Special Pythagorean triplet

for a in range(1, 332):
    for b in range(a, 1000 - a):
        c = 1000 - a - b
        if a ** 2 + b ** 2 == c ** 2:
            print(a, b, c)
            print("Product: {}".format(a * b * c))