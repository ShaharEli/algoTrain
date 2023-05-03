

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def kth_smallest(root, k):
    curr = root
    arr = []
    while curr:
        if curr.right is not None:
            arr.append(curr.right.value)
        arr.append(curr.value)
        curr = curr.left

    if k <= len(arr):
        return arr[len(arr) - k]
    curr = root.right
    K -= len(arr)
    arr = []
    while curr:
        if curr.right is not None:
            arr.append(curr.right.value)
        arr.append(curr.value)
        curr = curr.left

    if k <= len(arr):
        return arr[len(arr) - k]


root = TreeNode(8)
root.left = TreeNode(5)
root.right = TreeNode(14)
root.left.left = TreeNode(0)
root.left.right = TreeNode(6)
root.right.right = TreeNode(27)
root.right.right.right = TreeNode(300)
# print(kth_smallest(root, 5))


def map_tree_gen(root):
    if not root:
        return
    yield from map_tree_gen(root.left)
    yield root.value
    yield from map_tree_gen(root.right)


def kth_smallest2(root, k):
    mapped_tree = map_tree_gen(root)
    data = None
    for i in range(k):
        data = next(mapped_tree)
    return data


root = TreeNode(8)
root.left = TreeNode(5)
root.right = TreeNode(14)
root.left.left = TreeNode(0)
root.left.right = TreeNode(6)
root.right.right = TreeNode(27)
root.right.right.right = TreeNode(300)
# print(kth_smallest2(root, 2))


def map_collatz_helper(k, fun, length):
    if k == 1:
        fun(k)
        return length+1
    fun(k)
    next_val = k/2 if k % 2 == 0 else (3*k+1)
    return map_collatz_helper(next_val, fun, length+1)


def map_collatz(k, fun):
    return map_collatz_helper(k, fun, 0)


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data) + "->" + repr(self.next)


def split_sorted(head):
    heads = [head]
    curr = head
    while curr.next:
        next_node = curr.next
        curr_data = curr.data
        next_data = next_node.data
        if curr_data > next_data:
            curr.next = None
            heads.append(next_node)
        curr = next_node

    return heads


# my_node = Node(1, Node(2, Node(3, Node(2, Node(1, Node(10))))))
# print([repr(x) for x in split_sorted(my_node)])

# my_node2 = Node(1, Node(2, Node(3, Node(4))))
# print([repr(x) for x in split_sorted(my_node2)])

def guess_pass_helper(pwd, text, pwd_idx, text_idx, curr):
    if pwd_idx == len(pwd):
        return curr
    if text_idx == len(text):
        return False
    pwd_letter = pwd[pwd_idx]
    text_letter = text[text_idx]
    if pwd_letter == text_letter:
        return guess_pass_helper(pwd, text, pwd_idx+1, text_idx+1, curr+[text_idx])
    return guess_pass_helper(pwd, text, pwd_idx, text_idx+1, curr)


def guess_pass(pwd, text):
    if not text:
        return False
    return guess_pass_helper(pwd, text, 0, 0, [])


# pwd = "abc-123"
# text = "abc-123abc-123"
# x = guess_pass(pwd, text)
# print(x)


def n_of_sums_helper(n, start, fun, curr):
    next_val = fun(start)
    if curr == n:
        return 1
    if curr > n:
        return 0
    if start < 1:
        return 0

    return n_of_sums_helper(n, next_val, fun, curr+start) + n_of_sums_helper(n, next_val, fun, curr)


def n_of_sums(n, k, fun):
    return n_of_sums_helper(n, k, fun, 0)

#
# print(n_of_sums(12, 12, lambda b: b-2))
# print(n_of_sums(6, 4, lambda a: a-1))
