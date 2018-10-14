# Bình phương của tổng
square_of_summ = 0

# Tổng các bình phương
summ_of_square = 0

# Dùng for để tính tổng các bình phương và tổng các số cần tính
for i in range(1, 101):
    summ_of_square += i**2
    square_of_summ += i

# Tính ra bình phương của tổng các số đã tính ra ở trên
square_of_summ = square_of_summ**2

# Gía trị cần tìm chính là hiệu
print(square_of_summ - summ_of_square)