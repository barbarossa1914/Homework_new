class Node:

    def __init__(self, value):
        self.nref = None
        self.pref = None
        self.value = value


class DoublyLinkedList:
    def __init__(self):
        self.tail = Node(None)
        self.head = Node(None)

    def insert_in_tail(self, value):
        new_node = Node(value)
        if self.head.nref is None and self.head.value is None:
            self.tail.value = new_node.value
            self.head.value = new_node.value
        elif self.head.nref is not None:
            prev_node = self.tail
            self.tail = new_node
            prev_node.nref = self.tail
            self.tail.pref = prev_node
        else:
            prev_node = self.tail
            self.tail = new_node
            prev_node.nref = self.tail
            self.head.nref = self.tail
            self.tail.pref = prev_node

    def insert_in_head(self, value):
        new_node = Node(value)
        if self.head.value is None and self.head.nref is None:
            self.head = new_node
            self.tail = new_node
        else:
            next_node = self.head
            self.head = new_node
            self.head.nref = next_node
            next_node.pref = self.head

    def insert_in_position(self, value, position):
        n = self.head
        while position > 1:
            n = n.nref
            position -= 1
        new_node = Node(value)
        new_node.nref = n.nref
        n.nref = new_node
        new_node.pref = n
        n.nref.nref.pref = new_node

    def del_el_by_value(self, value):
        n = self.head
        if self.head.value == value:
            self.head = self.head.nref
        else:
            while n.nref.value != value:
                n = n.nref
            n.nref = n.nref.nref
            n.nref.nref.pref = n

    def find_by_value(self, value):
        n = self.head
        if n.value == value:
            return True
        else:
            while n.nref is not None and n.value != value:
                n = n.nref
            if n.value == value:
                return True
            else:
                return False

    def traverse_list(self):
        n = self.head
        while n is not None:
            print(n.value, " ")
            n = n.nref

    def traverse_reversed_list(self):
        n = self.tail
        while n is not None:
            print(n.value, ' ')
            n = n.pref

    def sequence(self, i):
        pos = 0
        n = self.head
        while pos != i:
            pos += 1
            n = n.nref
        while n is not None:
            print(n.value, ' ')
            n = n.nref


l = DoublyLinkedList()
l.insert_in_tail(4)
l.insert_in_tail(5)
l.insert_in_tail(3)
l.insert_in_tail(6)
l.insert_in_head(7)
l.insert_in_position(10, 2)
l.sequence(2)
l.traverse_list()
l.traverse_reversed_list()