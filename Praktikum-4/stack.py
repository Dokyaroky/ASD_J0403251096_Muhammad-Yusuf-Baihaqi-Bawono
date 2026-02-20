#=============================================================
# Nama  :
# NIM   :
# Kelas :
#=============================================================

#=============================================================
# Implemetasi Dasar : Node dan Linked List
#=============================================================

class Node:
    #konstruktor adalah fungsi yang dijalankan secara otomatis ketika class node dipanggil/instalasi
    def __init__(self, data):
        self.data = data # Menyimpan data pada list
        self.next = None # Pointer ke node berikutnya (awal=node)

#stack ada operasi Push(memasukan head baru) dan pop(menghapus head)

class Stack:
    def __init__(self):
        self.top = None #top menunjuk ke node paling atas (awalnya kosong)
    
    def is_empty(self):
        return self.top is None 
    
    def push(self, data):
        #1 membuat node baru
        nodeBaru = Node(data) #instantiasi/memanggil konstruktor pada class Node

        #2 node  baru menunjuk ke top yang lama(head lama)
        nodeBaru.next = self.top

        #3 geser top  pindah  ke node baru
        self.top = nodeBaru

    def tampilkan(self):
        #Top -> A -> B
        current = self.top
        print("Top -> ", end="")
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    
    def peek(self): #melihat data pada top tanpa menghapusnya
        if self.is_empty():
            return None
        return self.top.data

    
    def pop(self): #mengambil / menghapus node paling atas (top/head)

        if self.is_empty():
            print("Stack kosong, tidak bisa pop")
            return None

        data_terhapus = self.top.data #scroll bagian top dan simpan di variabel
        # B -> A -> None
        self.top = self.top.next 


#Instantiasi class stack
s = Stack()
s.push("A")
s.push("B")
s.push("C")
s.tampilkan()
print("Peed (Lihat Top)", s.peek())
s.pop()
s.tampilkan()
print("Peed (Lihat Top)", s.peek())