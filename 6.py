class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insert from end
    def insert_end(self, data):
        newnode = Node(data)

        if self.head is None:
            self.head = newnode
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = newnode

    # Delete from position
    def delete_position(self, pos):
        if self.head is None:
            print("List is empty")
            return

        if pos < 1:
            print("Invalid position")
            return

        if pos == 1:
            self.head = self.head.next
            return

        temp = self.head

        for i in range(pos - 2):
            if temp.next is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp.next is None:
            print("Invalid position")
            return

        temp.next = temp.next.next

    # Multiplication of all elements
    def multiply(self):
        product = 1
        temp = self.head

        while temp is not None:
            product = product * temp.data
            temp = temp.next

        print("Multiplication:", product)

    # Traverse
    def traverse(self):
        temp = self.head

        print("Linked List:", end=" ")
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Main program
sll = SinglyLinkedList()

sll.insert_end(2)
sll.insert_end(3)
sll.insert_end(4)

print("Original List:")
sll.traverse()

sll.delete_position(2)

print("After Deletion:")
sll.traverse()

sll.multiply()