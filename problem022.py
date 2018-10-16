# Tính tổng Name Score của danh sách 5000 tên
file_names = open("problem022_names.txt","r")

total_names = file_names.read().replace('"','').split(',')

print(*total_names)

