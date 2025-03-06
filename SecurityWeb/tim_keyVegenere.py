def khoa_Vige(ban_ma, ban_ro):
    # Tính toán sự dịch chuyển cho từng ký tự
    dich_chuyen = [(ord(ban_ma[i]) - ord(ban_ro[i])) % 26 for i in range(len(ban_ma))]

    # Chuyển dịch chuyển thành ký tự khóa
    khoa_tam = ''.join(chr(dc + ord('A')) for dc in dich_chuyen)

    # Tìm độ dài thực sự của khóa
    for do_dai_khoa in range(2, len(khoa_tam) + 1):
        if khoa_tam[:do_dai_khoa] == khoa_tam[do_dai_khoa:2 * do_dai_khoa]:
            return khoa_tam[:do_dai_khoa]

    return khoa_tam

ban_ma = input().strip()
ban_ro = input().strip()

khoa = khoa_Vige(ban_ma, ban_ro)
print(khoa)