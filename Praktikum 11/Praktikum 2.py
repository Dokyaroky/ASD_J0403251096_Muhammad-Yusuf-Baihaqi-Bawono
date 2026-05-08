#===========================================================
# Nama : Muhammad Yusuf Baihaqi Bawono
# NIM : J0403251096
# Kelas : TPL A1
#===========================================================
def createGraph(V, edges):
    adj = [[] for _ in range(V)]

    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    return adj

if __name__ == "__main__":
    V = 4

    nodes = ["A", "B", "C", "D"]

    edges = [
        [0, 1],  
        [0, 2],  
        [1, 3], 
        [2, 3]  
    ]

    adj = createGraph(V, edges)

    print("Adjacency List Representation:\n")

    for i in range(V):

        print(f"{nodes[i]} : ", end="")

        for j in adj[i]:
            print(nodes[j], end=" ")

        print()