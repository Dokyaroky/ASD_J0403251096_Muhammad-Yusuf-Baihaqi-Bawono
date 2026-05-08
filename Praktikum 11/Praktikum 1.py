#===========================================================
# Nama : Muhammad Yusuf Baihaqi Bawono
# NIM : J0403251096
# Kelas : TPL A1
#===========================================================

def createGraph(V, edges):
    mat = [[0 for _ in range(V)] for _ in range(V)]
    # Menambahkan setiap edge ke adjacency matrix
    for it in edges:
        # Mengambil simpul awal dari edge
        u = it[0]
        # Mengambil simpul tujuan dari edge
        v = it[1]
        # Menandai bahwa ada hubungan dari u ke v
        mat[u][v] = 1
        # Karena graph tidak berarah (undirected),
        # maka v juga terhubung ke u
        mat[v][u] = 1

    # Mengembalikan adjacency matrix yang sudah dibuat
    return mat

if __name__ == "__main__":

    # Jumlah vertex
    V = 4

    # Daftar edge/hubungan antar simpul
    edges = [[0, 1], [0, 2], [1, 2], [2, 3]]

    # Membuat graph menggunakan fungsi createGraph
    mat = createGraph(V, edges)

    # Menampilkan judul output
    print("Adjacency Matrix Representation:")

    # Loop untuk menampilkan setiap baris matriks
    for i in range(V):

        # Loop untuk menampilkan setiap kolom matriks
        for j in range(V):

            # Menampilkan isi matriks
            print(mat[i][j], end=" ")

        # Pindah ke baris baru setelah satu baris selesai
        print()