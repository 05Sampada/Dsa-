class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Insert from start
    def insert_start(self, data):
        newnode = Node(data)

        if self.head is None:
            self.head = newnode
            newnode.next = self.head
            return

        temp = self.head

        while temp.next != self.head:
            temp = temp.next

        newnode.next = self.head
        temp.next = newnode
        self.head = newnode

    # Insert from end
    def insert_end(self, data):
        newnode = Node(data)

        if self.head is None:
            self.head = newnode
            newnode.next = self.head
            return

        temp = self.head

        while temp.next != self.head:
            temp = temp.next

        temp.next = newnode
        newnode.next = self.head

    # Update specific position
    def update(self, pos, value):
        if self.head is None or pos < 1:
            print("Invalid position")
            return

        temp = self.head

        for i in range(pos - 1):
            temp = temp.next

            if temp == self.head:
                print("Invalid position")
                return

        temp.data = value

    # Traverse
    def traverse(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        print("Circular Linked List:", end=" ")

        while True:
            print(temp.data, end=" -> ")
            temp = temp.next

            if temp == self.head:
                break

        print("(Back to Head)")


# Main program
cll = CircularLinkedList()

cll.insert_start(20)
cll.insert_start(10)

cll.insert_end(30)

print("Original List:")
cll.traverse()

cll.update(2, 25)

print("After Updating:")
cll.traverse()