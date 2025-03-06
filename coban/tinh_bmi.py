#bài tập đầu tiên với ngôn ngữ python
cannang = float(input("Nhap can nang cua ban (kg): "))
chieucao = float(input("Nhap chieu cao cua ban (m): "))
bmi = cannang / (chieucao * chieucao)
print(f"Chi so BMI cua ban la: {bmi:.2f}")
if (bmi > 29):
    print("Ban beo phi")
else : print("Ban binh thuong")

