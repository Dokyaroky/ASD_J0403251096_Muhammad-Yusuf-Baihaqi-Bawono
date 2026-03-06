# ==========================================================
# Nama : Muhammad Yusuf Baihaqi Baawono
# NIM : J0403251096
# Kelas : TPL A1
# Studi Kasus: Generator PIN
# ==========================================================

def buat_pin(panjang, hasil=""):
    # Cek apakah panjang string hasil sudah sesuai target
    if len(hasil) == panjang:
        print("PIN:", hasil)
        return

    # Iterasi untuk setiap kemungkinan angka
    for angka in ["0", "1", "2"]:
        buat_pin(panjang, hasil + angka)

# Memanggil fungsi untuk menghasilkan PIN dengan panjang 3
buat_pin(3)

'''
Menambah program dengan mengecek data selanjutnya dan membandingkannya dengan data sebelumnya.
Apabila data sama, maka pin tersebut tidak memenuhi.
'''