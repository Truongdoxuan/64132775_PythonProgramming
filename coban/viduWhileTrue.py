"""viết chương trình Python cho phép lặp lại các thao tác nhập 1 số nguyên từ bàn phím, cho đến khi nhập 0 thì dừng
#tính tổng các số đã nhập
#tính trung bình cộng các số đã nhập
"""

# khai báo biến
tong = 0
n = 0
count = 0

# khởi tạo vòng lặp
while True:
    try:
        num = int(input("Nhập 1 số nguyên (nhập 0 để dừng): "))
        if num == 0:
            break
        tong += num
        count += 1 #n++
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ.")

# tính trung bình cộng
if count > 0:
    tbc = tong / count
else:
    tbc = 0

# kết thúc vòng lặp
print(f"Số lượng phần tử nhập vào = {count}")
print(f"Tổng các số đã nhập = {tong}")
print(f"Trung bình cộng các số đã nhập = {tbc}")



