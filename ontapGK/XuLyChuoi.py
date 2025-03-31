#nhập 1 chuỗi từ bàn phím
chuoi = input("Nhập vào 1 chuỗi (tối đa 100 ký tự): ")
while (len(chuoi) > 100):
    chuoi = input("Xin mời nhập lại 1 chuỗi (tối đa 100 ký tự): ")

# Kiểm tra chuỗi có rỗng không
if not chuoi.strip():
    print("Chuỗi nhập vào không hợp lệ! Vui lòng thử lại.")
else:
    #in ra man hinh
    print(chuoi)

    #đếm số từ trong chuỗi - split()
    print(f"Số lượng từ trong chuỗi là: {len(chuoi.split())}")

    #đếm số ký tự trong chuỗi - len()
    print(f"Số lượng ký tự trong chuỗi là: {len(chuoi)}")


    # kiểm tra chuỗi đối xứng
    def isChuoiDoiXung(str):
        return str == str[::-1]


    if isChuoiDoiXung(chuoi):
        print("Là chuỗi đối xứng")
    else:
        print("Không phải chuỗi đối xứng")

    #Trích xuất số từ chuỗi
    print("Các ký tự số có trong chuỗi trên là: ")
    for i in chuoi:
        if i.isdigit(): #isdigit() kiểm tra ký tự là số hay không
            print(i, end=" ")

    #đếm số lần xuất hiện của 1 ký tự
    kytu_chuoi = {} #dictionary luu so lan xuat hien
    for i in chuoi.lower(): #lower(): chuyển về chữ thường
        if i.isalnum():  #isalnum() chỉ đếm ký tự là chữ hoặc số không
            kytu_chuoi[i] = kytu_chuoi.get(i,0) + 1

    #Sắp xếp theo tần suất xuất hiện giảm dần
    tansuat_giam = sorted(kytu_chuoi.items(), key=lambda x: x[1], reverse=True)

    print("\nSố lần xuất hiện của ký tự trong chuỗi: ")
    for kytu, solan in tansuat_giam:
        print(f"Ký tự: {kytu} - Số lần: {solan}")

    #thay thế ký tự trong chuỗi
    vitri = int(input("Nhập vị trí ký tự muốn thay thế: "))
    kytu_moi = input("Ký tự mới thay thế: ")
    if 0 <= vitri < len(chuoi):
        chuoi_moi = list(chuoi) #chuyển thành list để thanh đổi
        chuoi_moi[vitri] = kytu_moi
        chuoi = ''.join(chuoi_moi) #nối lại thành chuỗi

        print(f"Chuỗi sau khi thay thế ký tự mới: {chuoi}")
    else:
        print("Vị trí không hợp lệ !")

    #loại bỏ ký tự đặc biệt khỏi chuỗi
    print("Chuỗi sau khi loại bỏ kí tự đặc biệt: ")
    for i in chuoi:
        if i.isalnum():
            print(i, end="")
        else:
            continue


