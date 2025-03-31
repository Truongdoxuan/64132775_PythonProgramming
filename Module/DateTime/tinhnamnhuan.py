import datetime
current_month = int(input("Nhap thang hien tai: "))
current_year = int(input("Nhap nam hien tai: "))

while(current_month not in [1,2,3,4,5,6,7,8,9,10,11,12]):
        current_month = int(input("Thang hien tai khong hop le. Vui long nhap lai: "))
if current_month in [1,3,5,7,8,10,12]:
    print(f"Thang {current_month} co 31 ngay")
elif current_month == 2 :
    if (current_year % 4 == 0 and current_year % 100 != 0):
        print(f"Thang {current_month} co 29 ngay")
        print(f"Nam {current_year} la nam nhuan")
    else:
        print(f"Thang {current_month} co 28 ngay")
elif current_month in [4, 6, 9, 11]:
    print(f"Thang {current_month} co 30 ngay")

