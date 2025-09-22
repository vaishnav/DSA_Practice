class SingleNode:
    def __init__(self, val):
        self.next = None
        self.data = val

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = SingleNode(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def prepend(self, data):
        new_node = SingleNode(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        current = self.head

        if current is None:
            print("List is empty, nothing to delete")
            return 

        if current and current.data == key:
            self.head = current.next
            current = None
            return

        prev = current
        current = current.next
        while current:
            if current.data == key:
                prev.next = current.next
                current = None
                return
            else:
                prev = current
                current = current.next

        print("key not found")
        return
    
    def display(self):
        current = self.head
        while current:
            print(f"{current.data}", end=" -> ")
            current = current.next


class DoubleNode:
    def __init__(self, val):
        self.next = None
        self.prev = None
        self.data = val