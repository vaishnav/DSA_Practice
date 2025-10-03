class SingleNode:
    def __init__(self, val):
        self.next = None
        self.data = val

    # Operator Overloading: Equality Check
    def __eq__(self, other):
        """
        Compare two linked lists for equality using == operator.

        Steps:
        1. Ensure 'other' is also a SingleNode (otherwise return False).
        2. Traverse both lists node by node.
        3. If any corresponding nodes have different data -> return False.
        4. If one list ends before the other -> return False.
        5. If both lists finish at the same time with all values equal -> return True.
        """
        if not isinstance(other, SingleNode):
            # Can't compare LinkedList with a non-LinkedList object
            return False
        
        current_self = self
        current_other = other
        
        # Traverse both lists simultaneously
        while current_self and current_other:
            if current_self.data != current_other.data:
                # Found a mismatch -> lists are not equal
                return False
            current_self = current_self.next
            current_other = current_other.next
        
        # Both must end at the same time to be equal
        return current_self is None and current_other is None
    
    def __str__(self):
        """
        Override print for Nodes
        """
        curr = self
        values = []
        while curr:
            values.append(str(curr.data))
            curr = curr.next
        return "".join(values)

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

    def appendList(self, elements: list):
        for element in elements:
            self.append(element)

    def getList(self):
        return self.head


class DoubleNode:
    def __init__(self, val):
        self.next = None
        self.prev = None
        self.data = val