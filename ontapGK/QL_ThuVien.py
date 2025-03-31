class Sach:
    # Constructor
    def __init__(self, masach, tensach, tacgia, sl_kho):
        self.masach = masach
        self.tensach = tensach
        self.tacgia = tacgia
        self.sl_kho = sl_kho

    # Kiểm tra sách còn hàng không
    def Ktra_Sach(self):
        return self.sl_kho > 0

# Danh sách sách
DS_Sach = [
    Sach("001", "A", "Peter", 10),
    Sach("002", "B", "Marry", 0),  # Sách này hết hàng
    Sach("003", "C", "John", 6),
    Sach("004", "D", "Will", 19),
    Sach("005", "E", "Lucy", 4),
    Sach("006","F","Peter", 8)
]

# Cập nhật số lượng sách
check = input("Bạn muốn mượn/trả ? (Mượn: 0, Trả: 1): ")

ms = input("Nhập mã sách: ")
found = False  # Biến kiểm tra sách có tồn tại không

if check == '0':  # Mượn sách
    for s in DS_Sach:
        if s.masach == ms:
            found = True
            if s.Ktra_Sach():
                s.sl_kho -= 1
                print(f"Mã sách {s.masach}: Số lượng kho {s.sl_kho}")
            else:
                print(f"Mã sách {s.masach} đã hết hàng!")
            break

elif check == '1':  # Trả sách
    for s in DS_Sach:
        if s.masach == ms:
            found = True
            s.sl_kho += 1
            print(f"Mã sách {s.masach}: Số lượng kho {s.sl_kho}")
            break

else:
    print("Lựa chọn không hợp lệ!")

if not found:
    print(f"Mã sách {ms} không tồn tại.")

#xóa cuốn sách nhập mã từ bàn phím với sl trong kho bằng 0
ma = input("Nhập mã sách bạn muốn xóa: ")
found = False
for s in DS_Sach:
    if s.masach == ma:
        found = True
        if s.sl_kho == 0:
            DS_Sach.remove(s)
            print(f"Mã sách {s.masach} đã được xóa")
            break
        else:
            print(f"Không thể xóa sách vì còn {s.sl_kho} cuốn")
            break
if not found:
    print(f"Mã sách {ma} không tồn tại")

#dictionary sl_sach
sl_sachtheoTG = {}
for s in DS_Sach:
    #nếu tác giả đã có trong từ điển -> cộng thêm sl sách vào kho
    if s.tacgia in sl_sachtheoTG:
        sl_sachtheoTG[s.tacgia] += s.sl_kho
    # ngược lại tạo key tác giả và gán gtri là sl sách đó trong kho
    else:
        sl_sachtheoTG[s.tacgia] = s.sl_kho

# Hiển thị danh sách số lượng sách theo từng tác giả
print("Số lượng sách của từng tác giả trong thư viện:")
for tacgia, so_luong in sl_sachtheoTG.items(): #item() trả về từng cặp key-value trong dict
    print(f"- {tacgia}: {so_luong} cuốn")