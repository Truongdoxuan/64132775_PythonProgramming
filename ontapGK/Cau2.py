#lớp sinh viên
class SinhVien:
    #phương thức khởi tạo
    def __init__(self, mssv, hoten, dsMon):
        self.mssv = mssv
        self.hoten = hoten
        self.dsMon = dsMon if dsMon is not None else {}

    #tính điểm trung bình tích lũy
    def tinhDTB(self):
        tong_diem = sum(self.dsMon.values())
        so_mon = len(self.dsMon)
        return round(tong_diem / so_mon,1)

    #in sinh vien
    def printSV(self):
        print(f"MSSV: {self.mssv}\t Họ tên: {self.hoten}\t Điểm trung bình tích lũy: {self.tinhDTB()}\n")

#danh sách sinh viên
SinhViens = [SinhVien("001", "A", {'mon1': 7.5, 'mon2': 6.7, 'mon3': 9.0}),
             SinhVien("002", "B", {'mon1': 6.5, 'mon2': 8.7, 'mon3': 7.0}),
             SinhVien("003", "C", {'mon1': 8.5, 'mon2': 7.7, 'mon3': 8.3} )]

#in danh sách sinh viên
print("Danh sách sinh viên: ")
for sv in SinhViens:
    sv.printSV()

#sắp xếp theo điểm trung bình tích lũy giảm dần
SinhViens.sort(key=lambda x: x.tinhDTB(), reverse=True)
print("Danh sách sắp sếp theo điểm trung bình tích lũy giảm dần: ")
for sv in SinhViens:
    sv.printSV()

#tìm kiếm sinh viên trong ds theo mã số nhập từ bàn phím
ms = input("Nhập mssv bạn muốn tìm kiếm: ")
found = False
for sv in SinhViens:
    if sv.mssv == ms:
        print(f"Thông tin sinh viên mã số {ms}:\n")
        sv.printSV()
        found = True
        break
if not found:
    print(f"Không tìm thấy sinh viên mã số {ms}")
