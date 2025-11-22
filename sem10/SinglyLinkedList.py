class Node:

    def __init__(self, value):
        self.nref = None
        self.value = value


class SinglyLinkedList:

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
        else:
            prev_node = self.tail
            self.tail = new_node
            prev_node.nref = self.tail
            self.head.nref = self.tail

    def insert_in_head(self, value):
        new_node = Node(value)
        if self.head.value is None and self.head.nref is None:
            self.head = new_node
            self.tail = new_node
        else:
            next_node = self.head
            self.head = new_node
            self.head.nref = next_node

    def insert_in_position(self, value, position):
        n = self.head
        while position > 0:
            n = n.nref
            position -= 1
        new_node = Node(n.value)
        new_node.nref = n.nref
        n.value = value
        n.nref = new_node

    def del_el_by_value(self, value):
        n = self.head
        if self.head.value == value:
            self.head = self.head.nref
        else:
            while n.nref.value != value:
                n = n.nref
            n.nref = n.nref.nref

    def find_by_value(self, value):
        n = self.head
        if n.value == value:
            return True
        else:
            while n.nref is not None and n.value is not value:
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


l = SinglyLinkedList()
l.insert_in_head(3)
l.insert_in_tail(5)
l.insert_in_head(4)
l.insert_in_tail(5)
print(l.find_by_value(3))
l.insert_in_position(7, 2)
l.del_el_by_value(3)
print(l.find_by_value(10))
l.traverse_list()
