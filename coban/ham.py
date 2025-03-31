# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 09:04:27 2025

@author: dxt81
"""
"""
#hàm in câu chào
def say_hi():
    print("Hi there !")
    
#gọi hàm
say_hi()

#cải thiện in ra câu chào 1 tên người cụ thể
def say_hi(name):
    print(f"Hello {name.title()}, nice to meet you !")

#gọi hàm
say_hi("Hello")
st = "Ronaldo"
say_hi(st)

#hàm xếp loại học tập
def xep_loai(diem_tb):
    #xet phai kieu float
    assert isinstance(diem_tb, float) and 0 <= diem_tb <= 10, "Diem khong hop le" #assert: condition, "message"
    return "Đạt" if diem_tb >= 5 else "Không đạt"

xl= xep_loai(7.0)
print(xl)

#ham kiem tra nhieu so
def swap(a,b):
    return b,a
x,y = 5,10
a,b = swap(x, y)
print(a,b)

"""

#ham co lenh tra ve yield
def generate_values():
    yield "Hello" #trả về giá trị này và dừng thực thi hàm đến khi Next() được gọi lại
    return "Nha Trang"
    yield 79
result = generate_values()
for r in result:
    print(r)
    
#ham tra ve tong cua n so nguyen tuy y
def tong(*values):
     return sum([i for i in values if isinstance(i, int)])
result1 = tong(1,2,3,4,5,6,"412")
print(result1)

#truyen doi tuong theo tu khoa
def print_student_info(**sv):
    print(f"MS: {sv['MS']}\tHo ten: {sv['HoTen']}\tDTB: {sv['DTB']}")
print_student_info(MS="64132775", HoTen="Xuan Truong", DTB=8.9)
#print_student_info(HoTen="Xuan Truong", DTB=8.9, MS="64132775")