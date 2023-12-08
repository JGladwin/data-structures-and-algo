class Node:
    val = None
    prev = None
    next = None

    def __init__(self, data = 0):
        self.val = data


class LinkedList:
    head = None
    tail = None
    length = 0

    def __init__(self, data = 0):
        self.head = Node(data)
        self.tail = self.head

        self.length += 1

    def push(self, data = 0):
        node = Node(data)
        node.prev = self.tail
        node.prev.next = node
        self.tail = node

        self.length += 1

    def pop(self):
        value = self.tail.val
        self.tail = self.tail.prev
        del self.tail.next
        print(self.tail.next.data)
        self.tail.next = None

        return value

    def insert(self, position, data = 0):
        node = Node(data)
        # position = 1, start of linked list
        if position == 1:
            node.next = self.head
            node.next.prev = node
            self.head = node

        # 1 < position < length of linkedlist
        elif 1 < position <= self.length:
            prev_node_pointer = self.head
            for _ in range(position-2):
                prev_node_pointer = prev_node_pointer.next

            node.prev = prev_node_pointer
            node.next = prev_node_pointer.next
            prev_node_pointer.next = node
            node.next.prev = node

            if position == self.length:
                self.tail = node.next

        else:
            self.push(data)

        self.length += 1

    def traverse(self): #  test function
        print("------------Traversal---------------------")
        pointer = self.head
        for i in range(self.length):
            print(pointer.val)
            pointer = pointer.next
        print("------------Traversal---------------------")

    #def pop(self):


obj1 = LinkedList(5)
print("\nPushed 5 into linked list\n")
print("Head(Value): " + str(obj1.head.val))

obj1.push(6)
print("\nPushed 6 into linked list\n")
print("Head(Value): " + str(obj1.head.val))
print("Second Node(Value): " + str(obj1.head.next.val))
print("Second Node(Value): " + str(obj1.tail.val))

obj1.push(7)
print("\nPushed 7 into linked list\n")
print("Third Node(Value) from head: " + str(obj1.head.next.next.val))
print("Third Node(Value) from tail: " + str(obj1.tail.val))

obj1.push(8)
print("\nPushed 8 into linked list\n")
obj1.traverse()
print("Fourth Node(Value) from head: " + str(obj1.head.next.next.next.val))
print("Fourth Node(Value) from tail: " + str(obj1.tail.val))

obj1.insert(position=3, data=9)
print("\nInserted 9 into linked list at position 3\n")
obj1.traverse()
print("Fifth Node(Value) from head: " + str(obj1.head.next.next.next.next.val))
print("Fifth Node(Value) from tail: " + str(obj1.tail.val))

obj1.insert(position=2, data=10)
print("\nInserted 10 into linked list at position 2\n")
obj1.traverse()
print("Sixth Node(Value) from head: " + str(obj1.head.next.next.next.next.next.val))
print("Sixth Node(Value) from tail: " + str(obj1.tail.val))

obj1.insert(position=1, data=11)
print("\nInserted 11 into linked list at position 1\n")
obj1.traverse()
print("Seventh Node(Value) from head: " + str(obj1.head.next.next.next.next.next.next.val))
print("Seventh Node(Value) from tail: " + str(obj1.tail.val))

print("Length of linked list is " + str(obj1.length))
obj1.insert(position=7, data=12)
print("\nInserted 12 into linked list at position 7\n")
obj1.traverse()
print("Eighth Node(Value) from head: " + str(obj1.head.next.next.next.next.next.next.next.val))
print("Eighth Node(Value) from tail: " + str(obj1.tail.val))

print("Popping one element")
obj1.pop()
obj1.traverse()
