# Distinct powers

list_terms = []

for a in range(2, 101):
    for b in range(2,101):
        if a ** b not in list_terms:
            list_terms.append(a**b)

print(len(list_terms))