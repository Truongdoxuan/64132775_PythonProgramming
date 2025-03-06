#ví dụ 1: viết chương trình yêu cầu người dùng nhập tên, năm sinh, in ra lời chào
#sử dụng thư viện thời gian để lấy năm hiện tại tự động

input()
chieucao = float(input("Nhập chiều cao của bạn (m): "))
cannang = float(input("Nhập cân nặng của bạn (kg): "))
bmi = round(cannang/(chieucao**2),1)
print(f"{bmi:g}")
if bmi < 18.5:
    print("Gầy(ốm)")
elif 18.5 <= bmi < 25:
    print("Bình thường")
elif 25 <= bmi < 30:
    print("Thừa cân")
else:
    print("Béo phì")
