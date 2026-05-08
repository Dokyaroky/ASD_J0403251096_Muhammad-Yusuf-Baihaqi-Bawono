#===========================================================
# Nama : Muhammad Yusuf Baihaqi Bawono
# NIM : J0403251096
# Kelas : TPL A1
#===========================================================
def createGraph(V, edges):

    adj = [[] for _ in range(V)]

    for it in edges:

        u = it[0]
        v = it[1]

        adj[u].append(v)

        adj[v].append(u)

    return adj

if __name__ == "__main__":

    nodes = ['A', 'B', 'C', 'D']

    V = 4

    edges = [
        [0, 1],  # A - B
        [0, 2],  # A - C
        [1, 2],  # B - C
        [2, 3]   # C - D
    ]

    adj = createGraph(V, edges)

    print("Adjacency List Representation:\n")

    for i in range(V):

        print(f"{nodes[i]} -> ", end="")

        for j in adj[i]:

            print(nodes[j], end=" ")

        print()