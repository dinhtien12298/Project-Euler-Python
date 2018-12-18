# Maximum path sum II

file = open("problem067.txt","r")

#Chia mỗi dòng thành 1 chuỗi nhỏ
number = file.read().strip().split('\n')

#Tiếp tục tách mỗi số trong chuỗi nhỏ ra và ép kiểu thành int, chuyển các chuỗi nhỏ thành list
for i in range(0,len(number)):
	number[i] = number[i].split(' ')
	number[i] = [int(x) for x in number[i]]

#Tính các đường đi từ chân tháp
for i in range(len(number)-2,-1,-1):
	for j in range(len(number[i])):
		number[i][j] = number[i][j] + max(number[i+1][j], number[i+1][j+1])

print(number[0][0])