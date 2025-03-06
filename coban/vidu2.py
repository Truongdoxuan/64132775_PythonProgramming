""" Xử lý chuỗi"""
s1 = "Welcome to Nha Trang City"
print(s1)
print(len(s1)) #đếm số ký tự trong chuỗi
for ch in s1: #in từng ký tự
    print(ch)
    #print(s1[10:]) #in từ ký tự thứ 10s
    #print(ch, end=" ") #w e l c o m e...
    
s2 = "The girl's name is Jane"
print(s2)

s3 = """
Tháng 3 mùa con ong đi lấy mật
Mùa con voi xuống sông xuống nước
"""
print(s3)

result1 = s3.find("voi")
print(result1) 
result2 = s3.replace("con", "chú")
print(result2)

s4 = """
Buồn trông cửa bể chiều hôm,
Thuyền ai thấp thoáng cánh buồm xa xa
Buồn trông ngọn nước mới sa
Hoa trôi man mác biết là về đâu
Buồn trông nội cỏ rầu rầu,
Chân mây mặt đất một màu xanh xanh
Buồn trông gió cuốn mặt duềnh
Ầm ầm tiếng sóng kêu quanh ghế ngồi
"""
words = [w.strip() for w in s4.split()] 
#split dùng để tách chuỗi thành danh sách các từ
#loại bỏ khoản trắng bằng strip
print(words) 
print(f"Tổng số từ = {len(words)}")

#đếm số lần xuất hiện của mỗi từ
#khởi tạo kiểu từ điển
word_count = {}
#xét từng từ trong danh sách
for w in words:
    #nếu ch có từ trong từ điển, đưa vào với số lượng =1
    if w not in word_count:
        word_count[w] = 1
    #ngược lại nếu đã có thì tăng số lượng lên
    else:
        word_count[w] += 1
for w in word_count:
    print(f"Từ '{w}' số lượng : {word_count[w]}")
    
#từ nào xuất hiện nhiều nhất
sorted_dict = {k: v for k, v in\
               sorted(word_count.items(),key=lambda item: item[1], reverse=True)}
print(list(sorted_dict.items())[0])