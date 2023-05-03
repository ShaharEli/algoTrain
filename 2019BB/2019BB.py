class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class LinkedList:
    def __init__(self, head):
        self.head = head


def is_bst_helper(node, less_then, greater_then):
    data = node.data
    if data == 7:
        print(less_then, greater_then)
    if less_then:
        if data > less_then:
            return False
    if greater_then:
        if data < greater_then:
            return False

    left, right = node.left, node.right
    if left and right:
        return is_bst_helper(node.left, data, greater_then) and is_bst_helper(node.right, less_then, data)
    if left:
        return is_bst_helper(node.left, data, greater_then)
    if right:
        return is_bst_helper(node.right, less_then, data)

    return True


ok = Node(6, Node(2, Node(1), Node(4, Node(3))), Node(8))
not_ok = Node(6, Node(2, Node(1), Node(4, Node(3), Node(7))), Node(8))


def is_bst(node):
    if not node:
        return True
    return is_bst_helper(node, None, None)


print(is_bst(ok))
print(is_bst(not_ok))


# def best_sum(lst, n):
#     setted_lst = list({x for x in lst if x <= n})
#     if sum(setted_lst) <= n:
#         return setted_lst[:]
#     arr = []
#     for elm in setted_lst:
#         setted_lst.remove(elm)
#         arr = [*arr, *best_sum(setted_lst, n-elm)]
#         arr.append(best_sum(setted_lst, n))
#         setted_lst.append(elm)
#     best = 0
#     elm = []
#     for elment in arr:
#         if not isinstance(elment, list) and not isinstance(elment, set):
#             elment = [elment]
#         if sum(elment) > best:
#             best = sum(elment)
#             elm = elment

#     return set(elm)
def best_sum(lst, n):
    setted_lst = list({x for x in lst if x <= n})
    if sum(setted_lst) <= n:
        return set(setted_lst)
    tail = setted_lst.pop()
    without_tail = best_sum(setted_lst, n)
    with_tail = set([tail]).union(best_sum(setted_lst, n-tail))
    if sum(without_tail) > sum(with_tail):
        return without_tail
    return with_tail


print(
    best_sum([1], 13)
)


def max_sum_path_helper(node, curr, arr):
    node_left = node.left
    node_right = node.right
    if not node_left and not node_right:
        curr.append(node.data)
        arr.append((sum(curr[:]), curr[:]))
        curr.pop()
    if node.right:
        curr.append(node.data)
        max_sum_path_helper(node.right, curr, arr)
        curr.pop()
    if node.left:
        curr.append(node.data)
        max_sum_path_helper(node.left, curr, arr)
        curr.pop()


def max_sum_path(node):
    arr = []
    max_sum_path_helper(node, [], arr)
    return max(arr, key=lambda x: x[0])


# root = Node(8, Node(2, Node(1, Node(0)), Node(
#     7, None, Node(4))), Node(5, Node(3), Node(2)))
# print(max_sum_path(root))
# (21, [8, 2, 7, 4])
class Polynomial:
    def __init__(self, ans):
        self.ans = ans

    def get_degree(self):
        if len(self.ans) == 0:
            return 0
        for i in range(len(self.ans)):
            if self.ans[i]:
                return len(self.ans)-1-i
        return 0

    def __add__(self, q):
        longest = max(len(self.ans), len(q.ans))
        my_ans = self.ans[:]
        q_ans = q.ans[:]
        while len(my_ans) < longest:
            my_ans.insert(0, 0)
        while len(q_ans) < longest:
            q_ans.insert(0, 0)
        return Polynomial(list(map(lambda x, y: x+y, my_ans, q_ans)))

    def get_derivative(self):
        new_ans = []
        for idx, an in enumerate(self.ans):
            new_ans.append((len(self.ans)-1-idx)*an)
        return Polynomial(new_ans)


# pol = Polynomial([2, 0, 0, 3, 1, 0])
# pol2 = Polynomial([0, 3, 1, 0])
# print((pol+pol2).ans)
# print(pol.get_derivative().ans)


def pasc_row_helper(n, j):
    if n == 0 or n == 1:
        return 1
    if j >= n or j <= 0:
        return 1
    return (pasc_row_helper(n-1, j-1) + pasc_row_helper(n-1, j))


def pasc_row(n):
    yield [pasc_row_helper(n, i) for i in range(n+1)]
    yield from pasc_row(n+1)


# hi = pasc_row(0)
# print(next(hi))
# print(next(hi))
# print(next(hi))
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def spare(L, pr):
    head_false = None
    curr_false = None
    head_true = None
    curr_true = None
    curr = L.head
    while curr:
        if pr(curr.value):
            if not head_true:
                head_true = curr
                curr_true = curr
            else:
                curr_true.next = curr
                curr_true = curr_true.next
        else:
            if not head_false:
                head_false = curr
                curr_false = curr
            else:
                curr_false.next = curr
                curr_false = curr_false.next
        curr = curr.next
    if curr_true:
        curr_true.next = None
    if curr_false:
        curr_false.next = None

    return LinkedList(head_true), LinkedList(head_false)


L = LinkedList(Node(2, Node(12, Node(1, Node(11)))))
T, F = spare(L, lambda x: x % 2 == 0)
curr = T.head
while curr:
    print(curr.value)
    curr = curr.next

curr = F.head
while curr:
    print(curr.value)
    curr = curr.next
