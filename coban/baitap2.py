ds = [3, {'64132775': {'name': 'Đỗ Xuân Trường', 'age': 21}},
5,(1,3,5,4), ['dưa hấu', 'nho', 'dâu', 'chanh dây'], 79, 'Nha Trang']
#tính tổng các số nguyên và tạo thành danh sách chỉ chứa số nguyên
tong_soNguyen = 0
ds_soNguyen = []
for n in ds:
    if isinstance(n, int): #kiểm tra phần tử là số nguyên
        tong_soNguyen += n
        ds_soNguyen.append(n)
print("Tổng các số nguyên = ", tong_soNguyen)
print("Danh sách kiểu số nguyên: ", ds_soNguyen)
