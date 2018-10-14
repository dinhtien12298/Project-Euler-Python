loop = True
list_tri_number = []

i = 1

while loop:
    print(i)
    list_factors = []
    for j in range(1,i):
        if i % j == 0 and j not in list_factors:
            list_factors.append(j)
            list_factors.append(i//j)

    k = 1    
    if len(list_factors) > 500:
        print(i)
        break
     
    i += 1


#         while k <= i:
#             list_tri_number.append(i)
#             i -= (len(list_tri_number) + 1)
#     list_tri_number.append(i)
#     i += (len(list_tri_number) + 1)

#     n = list_tri_number[-1]
#     print(n)

#     list_factors = []
#     for j in range(1,n):
#         if n % j == 0 and j not in list_factors:
#             list_factors.append(j)
#             list_factors.append(n//j)
    
#     if len(list_factors) > 500:
#         break
#     print(len(list_factors))

# print(list_tri_number[-1])

