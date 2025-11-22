class Node:

    def __init__(self, value, child1=None, child2=None):
        self.child1 = child1
        self.child2 = child2
        self.value = value


root = Node(1)
root.child1 = Node(2)
root.child2 = Node(3)
root.child1.child1 = Node(1)
root.child1.child2 = Node(2)
root.child2.child1 = Node(3)
root.child2.child2 = Node(4)

root1 = Node(1)
root1.child1 = Node(2)
root1.child2 = Node(2)
root1.child1.child1 = Node(1)
root1.child1.child2 = Node(2)
root1.child2.child1 = Node(3)
root1.child2.child2 = Node(4)


def is_mirror(tree1, tree2):
    if tree1 is None and tree2 is None:
        return True

    if tree1 is None or tree2 is None:
        return False
    if tree1.value == tree2.value:
        return (is_mirror(tree1.child1, tree2.child2)
                and is_mirror(tree1.child2, tree2.child1))
    else:
        return False


print(is_mirror(root.child1, root.child2))


def turn_to_mirror(tree):
    if tree is None:
        return
    tree.child1, tree.child2 = tree.child2, tree.child1
    turn_to_mirror(tree.child1)
    turn_to_mirror(tree.child2)


turn_to_mirror(root)
print(is_mirror(root, root1))


def find_parents(tree, value):
    if tree is None:
        return None

    if tree.value == value:
        return []

    left_parents = find_parents(tree.child1, value)
    if left_parents is not None:
        return [tree.value] + left_parents
    right_parents = find_parents(tree.child2, value)
    if right_parents is not None:
        return [tree.value] + right_parents


print(find_parents(root, 4))
