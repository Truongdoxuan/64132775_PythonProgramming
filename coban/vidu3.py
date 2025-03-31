# -*- coding: utf-8 -*-
"""
Kiểu tập hợp, danh sách

@author: dxt81
"""


fruits = ["apple", "banana", "apple", "kiwi", "orange"]
for f in fruits:
    print(f)
fruit_set = set(fruits) #tạo ra 1 set trái cây kh lấy ptu trùng lặp
print(fruit_set)   

s1 = {1,2,3,4}
s2 = {3,4,5,6,7,8}
u = s1.union(s2) #phép hợp
print(u) 

giao = s1.intersection(s2) #phép hợp
print(giao)

hieu1 = s1 - s2 #có trong s1 nhưng kh có trong s2
print(hieu1)

hieu2 = s2 - s1 #có trong s2 nhưng kh có trong s1
print(hieu2)

numbers = [1,2,'34',56,'57A']
print(len(numbers))
for i in numbers:
    print(i)
    
for i in range(len(numbers)):
    print(numbers[i])

#thêm phần tử
numbers.append(123)
print(numbers)
#xóa phần tử có giá trị bằng 1
numbers.remove(123)
print(numbers)
#tính tổng các phần tử
s = sum([i for i in numbers if isinstance(i, int)])
print(f"Tổng = {s}")

students = [
    {"name": "Alice", "score": 90},
    {"name": "Bob", "score": 85},
    {"name": "Charlie", "score": 95}
]

sorted_students = sorted(students, key=lambda x: x["score"], reverse=True)
print(sorted_students)
# Output: [{'name': 'Bob', 'score': 85}, {'name': 'Alice', 'score': 90}, {'name': 'Charlie', 'score': 95}]
