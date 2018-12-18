# Smallest multiple

# Nhập vào dãy số
sequence = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# Tạo ra các List và Dictionary để check và add các ước và số mũ
# List chứa các dictionary, mỗi dictionary có key và value là thừa số nguyên tố và số mũ của nó khi phân tích từng số trong dãy
list_number = []
dict_number = {}
list_key = []

# Thuật toán thêm vào list_number các dictionary thỏa mãn miêu tả trên, ta sẽ có các thừa số nguyên tố và số mũ khi phân tích từng số trong dãy
for number in sequence:
    dict_number = {}
    i = 1
    while i <= number:
        if number % i == 0:
            if i not in list_key:
                list_key.append(i)
                dict_number[i] = 1
            else:
                ex_number = 0
                for key, value in dict_number.items():
                    if key == i:
                        ex_number = value
                dict_number[i] = ex_number + 1
            if i == 1:
                i += 1
            else:
                number = number / i
        else:
            i += 1
    list_number.append(dict_number)

# Tạo ra 1 dictionary (list_result) chứa key là các thừa số nguyên tố, value là số mũ lớn nhất sau khi tổng hợp từ list_number
list_result = {}
for item in list_key:
    list_result[item] = 1
# Thuật toán lấy ra giá trị lớn nhất của số mũ để gán vào value của key là 1 thừa số nguyên tố
for key, value in list_result.items():
    for index1, item1 in enumerate(list_number):
        for key1, value1 in item1.items():
            if key1 == key and value1 > value:
                list_result[key] = value1
                value = value1

# Thuật toán tính tích của các thừa số nguyên tố với số mũ lớn nhất
scale = 1
for key2, value2 in list_result.items():
    scale *= key2 ** value2

# Kết quả chính là giá trị cần tìm
print(scale)