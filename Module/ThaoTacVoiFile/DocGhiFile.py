#tạo file và ghi nội dung
import os.path

with open("ghifile.txt", "w") as file:
    file.write("File created")
print("File được tạo và ghi dữ liệu")

#ghi thêm dữ liệu vào file
with open("ghifile.txt", "a") as file:
    file.write("\nWrite continue")

a = "1,2,3,4,5,6,7,8,9,10"
with open("docfile.txt", "w") as file1:
    for i in a:
        file1.write(i)
print("Ghi thanh cong")

#đọc dữ liệu từ file
with open("docfile.txt", "r") as file2:
    content = file2.read()
print(f"Noi dung cua file: {content}")

"""
Mở file với mã hóa utf-8 để hỗ trợ Unicode - encoding="utf-8"
with open("DocGhiFile.txt", "w", encoding="utf-8") as file:
    file.write("Đọc ghi file")  # Ký tự Unicode được ghi chính xác
print("Ghi dữ liệu thành công!")
"""

#ghi dữ liệu từ file có sẵn vào file mới chưa tạo mới
with open("docfile.txt", "r") as file3:
    content1 = file3.read()
with open("ghifile1.txt", "w") as file4:
    file4.write(content1)
print("ghi dữ liệu từ file có sẵn vào file mới chưa tạo mới thành công")

#xử lý lỗi khi làm việc với file
if os.path.exists("docfile.txt"):
    with open("docfile.txt", "a") as file5:
        file5.write("\nNew message")
else:
    print("No found")