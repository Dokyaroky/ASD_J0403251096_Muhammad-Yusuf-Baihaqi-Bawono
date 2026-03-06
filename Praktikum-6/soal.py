#Nama : Muhammad Yusuf Baihaqi Bawono
#NIM : J0403251096
#Kelas : TPL A1

#Latihan

data = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]

def bubbleSort(data):
    for passnum in range(len(data) - 1, 0, -1):
        for i in range(passnum):
            if data[i] < data[i + 1]:
                # Tukar dua data bersebelahan yang urutannya salah
                temp = data[i]
                data[i] = data[i + 1]
                data[i + 1] = temp
    return data

def top5(data):
    sorted_data = bubbleSort(data)
    print("Data setelah diurutkan secara descending:")
    print(sorted_data)

    print(f"\nLima kandidat yang lolos seleksi: {sorted_data[:5]}")

    for i in range(5):
        print(f"{i + 1}. {sorted_data[i]}")
    return sorted_data

data_sorted = top5(data)

print(f"Lima kandidat yang lolos seleksi: {data_sorted[:5]}")
print(f"Banyak kandidat yang lolos seleksi: {len(data_sorted[:5])}")

