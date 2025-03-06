def giai_ma_ceasar(ban_ma):
    tu_dien = {"AN", "BAN", "BUA", "CHAO", "DANG", "DUNG", "GAP", "HEN", "HOM", "KHOE", "KHONG", "LAI", "MOI", "MUA",
               "NAM", "NANG", "NAY", "NGAY", "SANG", "THOI", "TIET", "TOI", "TROI", "VIET", "YEU"}

    for khoa in range(26):
        ban_ro = ""
        for ky_tu in ban_ma:
            if 'a' <= ky_tu <= 'z':
                ban_ro += chr((ord(ky_tu) - ord('a') - khoa) % 26 + ord('a'))
            elif 'A' <= ky_tu <= 'Z':
                ban_ro += chr((ord(ky_tu) - ord('A') - khoa) % 26 + ord('A'))
            else:
                ban_ro += ky_tu

        cac_tu = ban_ro.split()
        if all(tu.upper() in tu_dien for tu in cac_tu):
            return ban_ro

    return "Không tìm thấy bản rõ hợp lệ"

ban_ma = input()
ban_ro = giai_ma_ceasar(ban_ma)
print(ban_ro)