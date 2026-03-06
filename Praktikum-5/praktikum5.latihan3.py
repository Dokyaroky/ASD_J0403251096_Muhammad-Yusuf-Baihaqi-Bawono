# ==========================================================
# Nama : Muhammad Yusuf Baihaqi Baawono
# NIM : J0403251096
# Kelas : TPL A1
# Latihan 3: Mencari Nilai Maksimum
# ==========================================================

def cari_maks(data, index=0):

    # Base case
    if index == len(data) - 1: 
        return data[index]

    # Recursive case
    maks_sisa = cari_maks(data, index + 1) #Fungsi rekursif

    if data[index] > maks_sisa: 
        return data[index]
    else:
        return maks_sisa


angka = [3, 7, 2, 9, 5]
print("Nilai maksimum:", cari_maks(angka))

'''
Pada Base Case, apabila panjang data hanya berisi 1 data. Maka output adalah angka itu sendiri
Pada Recursive Case, maks_sisa merupakan nilai terakhir. Yang dibandingkat terus menerus sampai kembali ke Rekursif Pertama.
Apabila angka pada titik data tertentu lebih besar dari maks_sisa maka maks_sisa menjadi nilai data tersebut.
'''

