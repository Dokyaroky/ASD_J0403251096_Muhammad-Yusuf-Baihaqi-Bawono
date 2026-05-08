#===========================================================
# Nama : Muhammad Yusuf Baihaqi Bawono
# NIM : J0403251096
# Kelas : TPL A1
#===========================================================

# Adjacency List
graph = {
    "Jakarta": ["Bandung", "Banten", "Bogor"],
    "Bandung": ["Jakarta", "Indramayu", "Cirebon"],
    "Banten": ["Jakarta", "Bogor"],
    "Bogor": ["Jakarta", "Banten"],
    "Indramayu": ["Bandung", "Cirebon"],
    "Cirebon": ["Bandung", "Indramayu"]
}

# Nama node
nodes = [
    "Jakarta",
    "Bandung",
    "Banten",
    "Bogor",
    "Indramayu",
    "Cirebon"
]

# Adjacency Matrix
matrix = [
#           JKT BDG BTN BGR IDM CRB
    [0, 1, 1, 1, 0, 0],  # Jakarta
    [1, 0, 0, 0, 1, 1],  # Bandung
    [1, 0, 0, 1, 0, 0],  # Banten
    [1, 0, 1, 0, 0, 0],  # Bogor
    [0, 1, 0, 0, 0, 1],  # Indramayu
    [0, 1, 0, 0, 1, 0]   # Cirebon
]

# =========================================
# MENAMPILKAN ADJACENCY LIST
# =========================================

print("=== ADJACENCY LIST ===\n")

for node, neighbors in graph.items():
    print(f"{node} -> {', '.join(neighbors)}")

# =========================================
# MENAMPILKAN ADJACENCY MATRIX
# =========================================

print("\n=== ADJACENCY MATRIX ===\n")

# Header kolom
print(f"{'':12}", end="")
for node in nodes:
    print(f"{node:<12}", end="")
print()

# Isi matrix
for i in range(len(matrix)):
    print(f"{nodes[i]:<12}", end="")

    for j in range(len(matrix[i])):
        print(f"{matrix[i][j]:<12}", end="")

    print()

# =========================================
# MENAMPILKAN HUBUNGAN ANTAR NODE
# =========================================

print("\n=== HUBUNGAN ANTAR NODE ===\n")

for node, neighbors in graph.items():
    for neighbor in neighbors:
        print(f"{node} terhubung dengan {neighbor}")