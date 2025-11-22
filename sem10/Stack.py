class Node:

    def __init__(self, value):
        self.nref = None
        self.pref = None
        self.value = value


class Stack:

    def __init__(self):
        self.tail = Node(None)
        self.head = Node(None)

    def push(self, value):
        new_node = Node(value)
        if self.head.value is None and self.head.nref is None:
            self.head = new_node
            self.tail = new_node
        else:
            next_node = self.head
            self.head = new_node
            self.head.nref = next_node
            next_node.pref = self.head

    def pop(self):
        n = self.head
        n.nref.pref = None
        self.head = n.nref

    def top(self):
        return self.head.value

    def size(self):
        s = 1
        n = self.head
        while n.nref is not None:
            n = n.nref
            s += 1
        return s

    def isempty(self):
        if self.head.value is None:
            return True
        else:
            return False

    def printstack(self):
        n = self.head
        while n is not None:
            print(n.value, " ")
            n = n.nref


l = Stack()
l.push(3)
l.push(4)
l.push(5)
l.pop()
print(l.top())
print(l.size())
print(l.isempty())
l.printstack()

ll = Stack()
print(ll.isempty())
