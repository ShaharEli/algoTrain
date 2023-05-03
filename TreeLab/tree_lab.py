class Node:

    def __init__(self, value, left=None, right=None):
        self.__value = value
        self.__left = left
        self.__right = right

    def get_left(self):
        return self.__left

    def get_right(self):
        return self.__right

    def get_value(self):
        return self.__value

    def set_value(self, value):
        self.__value = value


def print_tree(tree_node):
    if tree_node.get_left() is not None:
        print_tree(tree_node.get_left())
    print(tree_node.get_value(), end=" ")
    if tree_node.get_right() is not None:
        print_tree(tree_node.get_right())


def sum_tree(node):
    if node.get_left() and node.get_right():
        node.set_value(sum_tree(node.get_left()) +
                       sum_tree(node.get_right())+node.get_value())
    elif node.get_left():
        node.set_value(sum_tree(node.get_left()) +
                       node.get_value())
    elif node.get_right():
        node.set_value(sum_tree(node.get_right()) +
                       node.get_value())
    return node.get_value()


root = Node(9, Node(3, Node(1), Node(6, Node(4), Node(23))),
            Node(10, right=Node(14, Node(13))))
print_tree(root)

print()

x = sum_tree(root)
print_tree(root)
print(x)
