# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 15:52:14 2025

@author: dxt81
"""

# Danh sách chứa các danh sách các số nguyên
ds = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Tạo danh sách một chiều chứa các số chẵn
even_nums = []

# Duyệt qua từng danh sách con
for ls in ds:
    # Duyệt qua từng số trong danh sách con
    for n in ls:
        # Kiểm tra nếu số là chẵn
        if n % 2 == 0:
            even_nums.append(n)

print("even_nums =", even_nums)