# Tính tổng tất cả các kí tự của 2^1000

n = 2 ** 1000
sum = 0

digits = list(str(n))
for index, item in enumerate(digits):
    sum += int(item)

print(sum)