def chuan_hoa_ho_ten(ho_ten):
    ho_ten = ho_ten.strip()  # Loại bỏ khoảng trắng ở đầu và cuối
    ho_ten = " ".join(ho_ten.split())  # Xóa khoảng trắng thừa giữa các từ
    ho_ten = ho_ten.title()  # Viết hoa chữ cái đầu mỗi từ
    """
    ho_ten = ho_ten.lower().split()
    ho_ten = " ".join(word.capitalize() for word in ho_ten)  # Viết hoa thủ công
    """
    return ho_ten

# Nhập họ và tên
ho_ten = input("Nhập họ và tên: ")
ho_ten_chuan = chuan_hoa_ho_ten(ho_ten)

print(f"Họ và tên sau khi chuẩn hóa: {ho_ten_chuan}")

#xóa ký tự tại vị trí nhập vào
vitri = int(input("Nhập vào vị trí muốn xóa (bắt đầu từ 0): "))
if 0 <= vitri < len(ho_ten_chuan):
    chuoi_moi = ho_ten_chuan[:vitri] + ho_ten_chuan[vitri + 1:] #cắt chuỗi để loại bỏ ký tự tại vị trí
    print(f"Chuỗi sau khi xóa ký tự tại vị trí {vitri}: {chuoi_moi}")
else:
    print("Vị trí không hợp lệ !")