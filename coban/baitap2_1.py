"""
Created on Mon Mar  3 14:05:57 2025

@author: dxt81
"""

"""
Viết chương trình nhập vào một danh sách n số nguyên dương. Tạo một từ điển gồm n cặp <k,v> theo cấu trúc sau:

k: giá trị của phần tử (số nguyên)
v: là một danh sách chứa các thừa số nguyên tố của phần tử, theo thứ tự tăng dần.
Ví dụ:

numbers = [2, 12, 20]

thua_so = {2 : [2], 12: [2, 2, 3], 20: [2, 2, 5]}
"""

def listSNT(n):
    i = 2
    ds = []
    while i * i <= n:
        while (n % i) == 0:
            ds.append(i)
            n //= i
        i += 1
    if n > 1:
        ds.append(n)
    return ds

def dict_SNT(numbers):
    thua_so = {}
    for num in numbers:
        thua_so[num] = listSNT(num)
    return thua_so

# Nhập danh sách các số nguyên dương
try:
    numbers = list(map(int, input().split()))
    # Tạo từ điển thừa số nguyên tố
    thua_so = dict_SNT(numbers)

    # In kết quả
    print(thua_so)
except ValueError:
    print("Xin mời nhập lại")




        

