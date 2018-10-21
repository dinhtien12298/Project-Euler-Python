# Permuted multiples

i = 1
loop = True

while loop:
    check = 0
    for j in range(2,7):
        if len(str(i)) == len(str(j*i)):
            list1 = list(str(i))
            list2 = list(str(j*i))
            for index, item in enumerate(list1):
                if item in list2:
                    list2.remove(item)
            if len(list2) == 0:
                check += 1
        else:
            i += 1
    if check == 5:
        print(i)
        loop = False
    else:
        i += 1