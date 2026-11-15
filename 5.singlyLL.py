class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insert from start
    def insert_start(self, data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

    # Delete from end
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next.next is not None:
            temp = temp.next

        temp.next = None

    # Sum of elements
    def sum_elements(self):
        total = 0
        temp = self.head

        while temp is not None:
            total = total + temp.data
            temp = temp.next

        print("Sum:", total)

    # Traverse
    def traverse(self):
        temp = self.head

        if self.head is None:
            print("List is empty")
            return

        print("Linked List:", end=" ")
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

sll = SinglyLinkedList()

sll.insert_start(30)
sll.insert_start(20)
sll.insert_start(10)

print("After Insertion:")
sll.traverse()

sll.delete_end()
print("After Deletion:")
sll.traverse()

sll.sum_elements()