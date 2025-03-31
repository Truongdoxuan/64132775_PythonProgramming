import math
#hàm kiểm tra SNT
def isSNT(a):
    if a < 2:
        return False
    for i in range (2,int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True

#nhập số nguyên n từ bàn phím
n = int(input("Nhap n (5 < n < 1000): "))
while (n <= 5 or n >= 1000):
    n = int(input("Vui long nhap lai n (5 < n < 1000): "))

#in ra n SNT đầu tiên
print(f"{n} số nguyên tố đầu tiên là: ")
count = 0
num = 2
while count < n:
    if isSNT(num):
        print(num, end=" ")
        count += 1
    num += 1


#đếm số lượng SNT bé hơn n
dem = 0
for i in range(2,n):
    if isSNT(i):
        dem += 1
print(f"\nSố lượng số nguyên tố bé hơn {n} là: {dem}")
