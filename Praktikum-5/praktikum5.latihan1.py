# ==========================================================
# Nama : Muhammad Yusuf Baihaqi Baawono
# NIM : J0403251096
# Kelas : TPL A1
# Latihan 1: Rekursi Pangkat
# ==========================================================

def pangkat(a, n):
    # Base case
    if n == 0:
        return 1

    # Recursive case
    return a * pangkat(a, n - 1)


print(pangkat(2, 4))  # Output: 16

'''
Pada base case, apabila input yang dimasukkan adalah 0, output yang dihasilkan adalah 1.
Pada recursive case, nilai yang diinput akan dipangkat dengan fungsi yang dipanggil berulang
Pada contohnya pangkat(2,4), 2 dikalikan hingga 4 kali dengan memanggil fungsi kembali.
Hasilnya adalah 16.
'''