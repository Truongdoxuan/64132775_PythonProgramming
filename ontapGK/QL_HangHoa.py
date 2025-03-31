#class HangHoa
from struct import iter_unpack


class HangHoa:
    #phuong thuc khoi tao
    def __init__(self, mahang, tenhang, gia, soluong):
        self.mahang = mahang
        self.tenhang = tenhang
        self.gia = gia
        self.soluong = soluong

    #hien thi thong tin hang hoa
    def printInfo(self):
        print(f"Mã hàng: {self.mahang}\t Tên hàng: {self.tenhang}\t Giá: {self.gia}\t Số lượng: {self.soluong}")

#danh sach hang hoa
HangHoas = [HangHoa("001", "Apple", 5000, 10),
            HangHoa("002", "Banana", 5500, 9),
            HangHoa("003", "Kiwi", 7500, 11),
            HangHoa("004", "Lemon", 8000, 5)
            ]
#hien thi danh sach hang hoa
for hh in HangHoas:
    hh.printInfo()

mahang = input("Nhap ma hang: ")
tenhang = input("Nhap ten hang: ")
gia = int(input("Nhap gia: "))
soluong = int(input("Nhap so luong: "))

#tao doi tuong moi
hang_moi = HangHoa(mahang,tenhang,gia, soluong)
#them vao ds
HangHoas.append(hang_moi)

#hien thi danh sach hang hoa
for hh in HangHoas:
    hh.printInfo()