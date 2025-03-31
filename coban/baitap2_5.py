# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 16:00:19 2025

@author: dxt81
"""

# Danh sách chứa các ptu nhiều kiểu dữ liệu khác nhau
ds = [3, {'64132775': {'name': 'Đỗ Xuân Trường', 'age': 21}}, 
                5, (1, 3, 5, 4), ['dưa hấu', 'nho', 'dâu', 'chanh dây'], 79, 'Nha Trang']

# Tính tổng các số nguyên và tạo danh sách chỉ chứa số nguyên
tong_soNguyen = 0
ds_soNguyen = []

for n in ds:
    if isinstance(n, int):  # Kiểm tra nếu phần tử là số nguyên
        tong_soNguyen += n
        ds_soNguyen.append(n)

print("Tổng các số nguyên =", tong_soNguyen)
print("Danh sách các số nguyên: ", ds_soNguyen)

'''
python
'''