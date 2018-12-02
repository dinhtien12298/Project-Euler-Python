# Integer right triangles
t_max = 0
p_max = 0

for p in range(0, 1001, 2):
    t = 0
    for a in range(1, p/2):
        # b = p*(p - 2*a)/(2*(p - a))
        if p*(p - 2*a) % (2*(p - a)) == 0: 
            t += 1
            if t >= t_max:
                t_max = t
                p_max = p
 
print(p_max)