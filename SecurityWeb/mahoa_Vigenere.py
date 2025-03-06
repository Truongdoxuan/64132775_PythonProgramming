def mh_Vige(ban_ro, khoa):
    ban_ma = []
    khoa_dai = len(khoa)

    for i, ky_tu in enumerate(ban_ro):
        # Tính toán vị trí dịch chuyển dựa trên khóa
        khoa_vi_tri = ord(khoa[i % khoa_dai]) - ord('A')
        # Mã hóa ký tự
        ma_hoa_ky_tu = (ord(ky_tu) - ord('A') + khoa_vi_tri) % 26 + ord('A')
        ban_ma.append(chr(ma_hoa_ky_tu))

    return ''.join(ban_ma)

ban_ro = input().strip()
khoa = input().strip()

ban_ma = mh_Vige(ban_ro, khoa)
print(ban_ma)