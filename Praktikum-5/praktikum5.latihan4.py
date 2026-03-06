# ==========================================================
# Nama : Muhammad Yusuf Baihaqi Baawono
# NIM : J0403251096
# Kelas : TPL A1
# Latihan 4: Kombinasi Huruf
# ==========================================================

def kombinasi(n, hasil=""):
    # Base case: jika panjang string sudah mencapai n
    if len(hasil) == n:
        print(hasil)
        return

    # Rekursi: tambahkan "A" lalu "B" secara bergantian
    kombinasi(n, hasil + "A")
    kombinasi(n, hasil + "B")

# Memanggil fungsi dengan n = 2
kombinasi(2)

'''
Pada 1 kombinasi output yang dihasilkan adalah 2 angka
Pada 2 kombinasi output yang dihasilkan adalah 4 kombinasi
Pada 3 kombinasi output yang dihasilkan adalah 8 kombinasi
Dari pola diatas jumlah kombinasi yang dihasilkan mengikuti persamaan 2ⁿ.
'''