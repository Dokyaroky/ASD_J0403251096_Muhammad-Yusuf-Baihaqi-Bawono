class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    def delete_node(self, key):
        temp = self.head

        # Jika node pertama adalah yang ingin dihapus
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None

        # Mencari node yang ingin dihapus
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        # Jika key tidak ditemukan
        if temp is None:
            print(f"Elemen {key} tidak ditemukan dalam Linked List.")
            return

        # Hapus node
        prev.next = temp.next
        temp = None
    
        


# Contoh Penggunaan
ll = LinkedList()
ll.insert_at_end(3)
ll.insert_at_end(5)
ll.insert_at_end(13)
ll.insert_at_end(2)
ll.display()
ll.delete_node(5)
ll.delete_node(7)
ll.display()