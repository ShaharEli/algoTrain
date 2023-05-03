# class Node:
#     def __init__(self, data=None, next=None):
#         self.data = data
#         self.next = next


def shift(x, k):
    counter = 0
    curr = x
    prev = None
    while counter < k:
        prev = curr
        curr = curr.next
        counter += 1
    ref = curr
    prev.next = None
    while curr.next:
        curr = curr.next
    curr.next = x
    return ref


# root = Node(10, Node(20, Node(30, Node(40, Node(50, Node(60))))))


def printo(x):
    curr = x
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print()


# printo(root)

# printo(shift(root, 3))


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def max_sum_path_helper(node, curr_data):
    if not node:
        return curr_data
    left, right, data = node.left, node.right, node.data
    new_tup = (curr_data[0]+data, curr_data[1]+[data])
    left_check = max_sum_path_helper(left, new_tup)
    right_check = max_sum_path_helper(right, new_tup)
    if left_check[0] > right_check[0]:
        return left_check
    return right_check


def max_sum_path(root):
    res = max_sum_path_helper(root, [0, []])
    return res


root = Node(8, Node(2, Node(1, Node(0)), Node(
    7, None, Node(4))), Node(5, Node(3), Node(2)))
print(max_sum_path(root))
(21, [8, 2, 7, 4])
