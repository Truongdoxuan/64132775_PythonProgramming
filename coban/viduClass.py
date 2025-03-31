#Tạo lớp sinh viên
class SinhVien:
    """hàm thiết lập (Constructor)"""
    def __init__(self, ms, hoten, dtb):
        self.MS = ms
        self.HoTen = hoten
        self.DTB = dtb

    """hàm in thông tin"""
    def print_info(self):
        print(f"MSSV: {self.MS}\t Họ tên: {self.HoTen}\t Điểm trung bình: {self.DTB}")

#Tạo đối tượng
sv1 = SinhVien("64132775", "A", 8.9)
sv2 = SinhVien("64132776", "B", 7.3)
sv3 = SinhVien("64132777", "C", 8.4)
sv1.print_info()