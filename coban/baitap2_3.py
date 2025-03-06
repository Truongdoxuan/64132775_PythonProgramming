"""
Created on Mon Mar  3 15:19:19 2025

@author: dxt81
"""

a = input("Nhập dãy các từ cách nhau bởi dấu phẩy: ")

# Tách chuỗi thành danh sách các từ
words = a.split(", ") #"," làm dấu phân tách loại bỏ dấu , và khoản trắng khi nhập

# Sắp xếp theo thứ tự alphabet
words_sorted = sorted(words)

# Ghép danh sách đã sắp xếp thành một chuỗi
b = ", ".join(words_sorted) #thêm dấu , ngăn cách các từ
print(b)