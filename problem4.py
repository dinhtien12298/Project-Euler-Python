number = 0
# Dùng vòng for để duyệt các số được nhân từ các số có 3 chữ số lớn nhất và giảm dần
for i in range(999*999, 10000, -1):
    # Lọc ra các số có sự đối xứng
    digits = list(str(i))
    if len(digits) % 2 == 0 and digits[0] == digits[-1] and digits[1] == digits[-2] and digits[2] == digits[-3]:
        loop = True
    elif len(digits) % 2 != 0 and digits[0] == digits[-1] and digits[1] == digits[-2]:
        loop = True
    else:
        loop = False
    # Check xem số đó có là tích của 2 số có 3 chữ số không
    # Tăng 1 số j từ 100 đến 999 và nếu check được i chia hết cho j tìm gọi thương là k và check xem k có 3 chữ số hay không
    j = 100
    while j < 1000 and loop:
        if i % j != 0:
            j += 1
        else:
            k = i / j
            if 99 < k < 1000:
                print(i)
                number = i
                loop = False
            else:
                j += 1
    # Khi check được số, gán bằng một giá trị bên ngoài để dừng vòng for
    if number != 0:
        break

# Gía trị cần tìm chính là i đã được print