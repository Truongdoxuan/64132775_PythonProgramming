def chuan_hoa_ho_ten(ho_ten):
    ho_ten = ho_ten.strip()  # Loại bỏ khoảng trắng ở đầu và cuối
    ho_ten = " ".join(ho_ten.split())  # Xóa khoảng trắng thừa giữa các từ
    ho_ten = ho_ten.title()  # Viết hoa chữ cái đầu mỗi từ
    return ho_ten

# Nhập họ và tên
ho_ten = input("Nhập họ và tên: ")
ho_ten_chuan = chuan_hoa_ho_ten(ho_ten)

print(f"Họ và tên sau khi chuẩn hóa: {ho_ten_chuan}")
