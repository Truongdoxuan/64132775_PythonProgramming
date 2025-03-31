#class NhanVien

class NhanVien:
    def __init__(self, manv, hoten, chucvu, luong):
        self.manv = manv
        self.hoten = hoten
        self.chucvu = chucvu
        self.luong = luong

    def printInfo(self):
        print(f"Mã nhân viên: {self.manv}\t Họ tên: {self.hoten}\t Chức vụ: {self.chucvu}\tLương: {self.luong}")

#ds nhan vien
NhanViens = [NhanVien("001", "A", "Nhan vien", 6000),
             NhanVien("002", "B", "Ke toan", 6500),
             NhanVien("003", "C", "Pho giam doc", 7500),
             NhanVien("004", "D", "Truong phong", 7000),
             NhanVien("005", "E", "Giam doc", 9000),
             NhanVien("006", "F", "Pho giam doc", 7500),
             NhanVien("007", "G", "Nhan vien", 6000),
             NhanVien("008", "H", "Nhan vien", 6000),
             NhanVien("009", "I", "Nhan vien", 6000),
             NhanVien("010", "J", "Nhan vien", 6000),
             ]
for nv in NhanViens:
    nv.printInfo()

#sap xep theo luong giam dan
print("Danh sách khi sắp xếp theo lương giảm dần như sau:")
sorted_luong = NhanViens.sort(key=lambda x:x.luong, reverse=True)
for nv in NhanViens:
    nv.printInfo()

#tim kiem nhan vien theo manv
ma = input("Nhập mã nhân viên muốn tìm kiếm: ")
found = False
for nv in NhanViens:
    if nv.manv == ma:
        print(f"Thông tin nhân viên mã số {nv.manv}: ")
        nv.printInfo()
        found = True
if not found:
    print(f"Mã {ma} không tồn tại")

#dem sl nhan vien theo chuc vu
sl_nv_theochucvu = {}
count = 0
for nv in NhanViens:
    if nv.chucvu in sl_nv_theochucvu:
        count += 1
        sl_nv_theochucvu[nv.chucvu] = count
    else:
        count = 1
        sl_nv_theochucvu[nv.chucvu] = count

print("Thống kê nhân viên theo chức vụ: ")
for chucvu, soluong in sl_nv_theochucvu.items():
    print(f"{chucvu}: {soluong} người")

#cập nhật mức lương của nhân viên theo mã số nv
check = input("Chọn chức năng (0: cập nhật lương, 1: xóa nhân viên): ")
if check == '0':
    ms = input("Nhập mã số nhân viên muốn cập nhật mức lương: ")
    luong_new = int(input("Nhập mức lương mới: "))
    for nv in NhanViens:
        if nv.manv == ms:
            found = True
            nv.luong = luong_new
            print(f"Cập nhật mức lương mới {nv.luong} mã số {nv.manv}")
            break
elif check == '1':
    ms = input("Nhập mã số nhân viên muốn xóa: ")
    for nv in NhanViens:
        if nv.manv == ms:
            NhanViens.remove(nv)
            print(f"Xóa thành công nhân viên mã số {nv.manv}")
            break
    if not found:
        print(f"Mã số {ms} không tồn tại")

