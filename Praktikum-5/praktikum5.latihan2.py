# ==========================================================
# Nama : Muhammad Yusuf Baihaqi Baawono
# NIM : J0403251096
# Kelas : TPL A1
# Latihan 2: Tracing Rekursi
# ==========================================================

def countdown(n):
    if n == 0: #Jika input adalah 0 maka return dan outputnya "selesai".
        print("Selesai")
        return

    print("Masuk:", n)

    countdown(n - 1) #Memanggil fungsi rekursif

    print("Keluar:", n)


countdown(3) #Memanggil fungsi.

'''
Mengapa output keluar muncul terbalik?
Dikarenakan output masuk akan terus berulang hingga n = 0, sehingga masuk teroutput pertama.
Ketika n = 0, rekursif selesai dan baru mulai menjalankan program setelahnya, dimulai dari rekursif paling akhir.
Sehingga dimulai dari n = 1 (Rekursif terakhir), n = 2, n = 3 (Rekursif pertama).
'''