def mh_DonBang(ban_ro, khoa):
    # Tạo bảng thay thế từ bảng chữ cái thường sang khóa
    bang_thay_the = {chr(i + ord('a')): khoa[i] for i in range(26)}

    # Mã hóa bản rõ
    ban_ma = ""
    for ky_tu in ban_ro:
        if ky_tu.islower():  # Nếu là chữ cái thường
            ban_ma += bang_thay_the[ky_tu]
        else:  # Nếu là khoảng trắng hoặc ký tự khác
            ban_ma += ky_tu

    return ban_ma

ban_ro = input()
khoa = input()

ban_ma = mh_DonBang(ban_ro, khoa)
print(ban_ma)