# Sub-string divisibility

from itertools import permutations

p = permutations('0123456789')
sum = 0

for i in list(p):
    if (int(str(i[1])+str(i[2])+str(i[3])) % 2 == 0) and (int(str(i[2])+str(i[3])+str(i[4])) % 3 == 0) and (int(str(i[3])+str(i[4])+str(i[5])) % 5 == 0) and (int(str(i[4])+str(i[5])+str(i[6])) % 7 == 0) and (int(str(i[5])+str(i[6])+str(i[7])) % 11 == 0) and (int(str(i[6])+str(i[7])+str(i[8])) % 13 == 0) and (int(str(i[7])+str(i[8])+str(i[9])) % 17 == 0):
        sum += int(''.join(i))

print(sum)
