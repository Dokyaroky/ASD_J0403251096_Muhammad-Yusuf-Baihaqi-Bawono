#=================================================
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan   2: Membuat fungsi Load Data dari File
# =================================================

#variable menyimpan data file
nama_file = "Praktikum-2/data_mahasiswa.txt"

def baca_data(nama_file):
    data_dict = {}
    with open(nama_file,"r",encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            NIM,nama,nilai = baris.split(",")
            data_dict[NIM] = {"nama": nama, "nilai": int(nilai)}
    return data_dict

buka_data = baca_data(nama_file)
print("jumlah data terbaca", len(buka_data))


#=================================================
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan   2: Membuat Fungsi Menamilkan Data
# =================================================

def tampilkan_data(data_dict):
    #Membuat header tabel
    print("\n=== Daftar Mahasiswa ===")
    print(f"{'NIM' : <10} | {'Nama' : <12} | {'Nilai' : >5}")
    '''
    untuk tampilan yang rapi, atur lebar kolom
    {'NIM' : <10} artinya nim rata kiri dengan lebar kolom 10 karakter
    {'Nama' : <12} artinya nama rata kiri dengan lebar kolom 12 karakter
    {'Nilai' : >5} artinya nilai rata kanan dengan lebar kolom 5 karakter
    '''
    print("-"*35) #membuat garis 

    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f"{nim : <10} | {nama : <12} | {nilai : >5}")

#tampilkan_data(buka_data) #memanggil fungsi untuk menampilkan data

#=================================================
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan   3: Membuat Fungsi Mencari Data
# =================================================

#membuat fungsi pencarian data
def cari_data(data_dict):
    #pencarian data berdasarkan NIM sebagai key dictionary
    #membuat input NIM mahasiswa yang akan dicari
    nim_cari = input("\nMasukkan NIM yang ingin dicari: ").strip()

    if nim_cari in data_dict:
        nama =  data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]

        print("===== Data Mahasiswa Ditemukan =====")
        print(f"NIM  : {nim_cari}")
        print(f"Nama : {nama}")
        print(f"Nilai: {nilai}")
    else:
        print("Data tidak ditemukan. Pastikan NIM yang dimasukkan benar.")

#memanggil fugnsi cari data
#cari_data(buka_data)

#=================================================
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan   4: Membuat Fungsi Update Data
# =================================================

def ubah_data(data_dict):
    
    #awali dulu dengan mencari nim / data yang ingin di update

    nim = input("\nMasukkan NIM yang ingin diubah datanya: ").strip()

    if nim not in data_dict:
        print("NIM tidak ditemukan. Update dibatalkan.")
        return
    
    try:
        nilai_baru = int(input("Masukkan nilai baru 0-100: ").strip())
    except ValueError:
        print("Nilai harus berupa angka. Update dibatalkan.")
    
    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai harus antara 0-100. Update dibatalkan.")

    nilai_lama =  data_dict[nim]["nilai"]
    data_dict[nim]["nilai"] = nilai_baru

#ubah_data(buka_data) 
#=================================================
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan   5: Membuat Fungsi Menyimpan Data dalam FIle
# =================================================

def simpan_data(nama_file, data_dict):
    with open(nama_file,"w",encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim},{nama},{nilai}\n")
            print("\nData Berhasil Disimpan ke file: ", nama_file)

#memanggil fungsi simpan data
#simpan_data(nama_file, buka_data)


#=================================================
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan   6: Membuat Menu Interaktif
# =================================================

def main():
    #load data otomoatis saat program dimulai
    buka_data = baca_data(nama_file)

    while True:
        print("\n=== Menu Utama ===")
        print("1. Tampilkan Data Mahasiswa")
        print("2. Cari Data Bedasarkan NIM")
        print("3. Ubah Nilai Mahasiswa")
        print("4. Simpan data ke File")
        print("5. Keluar")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tampilkan_data(buka_data)
        elif pilihan == "2":
            cari_data(buka_data)
        elif pilihan == "3":
            ubah_data(buka_data)
        elif pilihan == "4":
            simpan_data(nama_file, buka_data)
        elif pilihan == "5":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()