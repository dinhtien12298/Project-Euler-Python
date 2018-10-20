# Có bao nhiêu số nằm trong chuỗi tạo thành từ a^b với 2 <= a,b <= 100

list_terms = []

for a in range(2, 101):
    for b in range(2,101):
        if a ** b not in list_terms:
            list_terms.append(a**b)

print(len(list_terms))