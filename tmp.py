# def invert_d(d):
#     return {v: [k for k, v2 in d.items() if v2 == v] for v in d.values()}


# d = {7: 1, 8: 2, 9: 3, 10: 3, 11: 2, 12: 2}
# print(invert_d(d))
from functools import reduce
import random


def f(k):
    if k > 0:
        yield from f(k-1)
        yield k
        yield from f(k-1)


def check(item, sett):
    if not isinstance(item, list):
        return
    if id(item) not in sett:
        sett.add(id(item))
        for i in item:
            check(i, sett)


def recursive_list_maker(k):
    if not k:
        return [k, []]
    result = [k, (k-1)*recursive_list_maker(k-1)]
    return result


lalaa = set()
res = recursive_list_maker(5)
check(res, lalaa)
# print(len(lalaa))

source = [1, 2]
source[1] = source
x = [[source[:] for _ in range(10)] for j in range(10)]
z = [i[:] for i in x]
lala = set()
check(x, lala)
lalaa = set()
check(z, lalaa)
# print(len(lala.difference(lalaa)))


def llala(n):
    lst = list()
    for i in range(n):
        lst.append(i)
        lst = lst[::-1]
    return lst


# print(llala(9))
vec = [0, 0, 6, 0, 3, 6]


def tr(ls):
    return {idx: elm for idx, elm in enumerate(ls) if elm != 0}


# print(tr(vec))
a = set()
b = set()


def check(x, sett):
    if isinstance(x, list):
        val = id(x)
        if val not in sett:
            sett.add(val)
            for i in x:
                check(i, sett)


def deepen(x, n):
    return [x[:] for _ in range(n)]


# n = 5
# lst1 = list(range(n))
# lst1.append(lst1)
# lst2 = deepen(lst1, n)
# check(lst2, a)
# lst3 = deepen(lst2, n)
# check(lst3, b)
# print(len(a))
# print(len(b))

ls = [1, -2, 0, 4, -5, 6, 0, 8, 9]
def g(x, y): return (x if x else 1)*(y if y else 1)


# print(reduce(g, ls))
d = {"c": 1}


def f(j):
    d["c"] += 1
    return (g(j))


def g(j):
    if j <= 0:
        return j
    d["c"] += 1
    return f(j-1)


# g(10)
# print(d)

def xyz_helper(num_x, num_y, num_z, curr, arr):
    if not num_x and not num_y and not num_z:
        arr.append(curr)
        return
    if num_x:
        xyz_helper(num_x-1, num_y, num_z, curr+"x", arr)
    if num_y:
        xyz_helper(num_x, num_y-1, num_z, curr+"y", arr)
    if num_z:
        xyz_helper(num_x, num_y, num_z-1, curr+"z", arr)


def xyz(num_x, num_y, num_z):
    arr = []
    xyz_helper(num_x, num_y, num_z, "", arr)
    return arr


# print(xyz(2, 0, 1))
class Node:
    def __init__(self, data, children=None):
        self.data = data
        if not children:
            children = []
        self.children = children[:]


tr = Node(1, [
    Node(2, [
        Node("a")
    ]),
    Node(3, [
        Node("b")

    ]),
    Node(4, [
        Node("c")
    ]),
])


def next_lv(nodes):
    for node in nodes:
        for child in node.children:
            yield child


# for n in next_lv(next_lv([tr])):
#     print(n.data)


def lexico_iter_helper(ls, length):
    if not length:
        yield ""
    elif length == 1:
        yield from (lett for lett in ls)
    else:
        yield from (lett + root for lett in ls for root in lexico_iter_helper(ls, length-1))


def lexico_iter(ls):
    i = 0
    while True:
        yield from lexico_iter_helper(ls, i)
        i += 1


# lala = lexico_iter(["a", "b", "c"])
# i = 40
# while i:
#     print(next(lala))

#     i -= 1


def count_strings_helper(n, prev):
    if n == 0:
        return 1
    if prev:  # prev=1
        return count_strings_helper(n-1, 0)
    return count_strings_helper(n-1, 0)+count_strings_helper(n-1, 1)
    # prev=0


def count_strings(n):
    print(
        count_strings_helper(n, 0)
    )
    return count_strings_helper(n, 0)


# count_strings(0)
# # good strings are: “”
# count_strings(1)
# # good strings are: “0”, “1”
# count_strings(2)
# # good strings are: “00”, “01”, “10”
# # but NOT “11”
# count_strings(3)
# good strings are: “000”
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def tree_gen(root):
    if not root:
        return
    yield from tree_gen(root.left)
    yield root.value
    yield from tree_gen(root.right)


root = TreeNode(8)
root.left = TreeNode(5)
root.right = TreeNode(14)
root.left.left = TreeNode(0)
root.left.right = TreeNode(6)
root.right.right = TreeNode(27)
root.right.right.right = TreeNode(300)


def kth_smallest(root, n):

    genert = tree_gen(root)
    val = None
    for i in range(n):
        val = next(genert)
    return val


# print(kth_smallest(root, 2))
def map_collatz_helper(n, f):
    f(n)
    if n == 1:
        return 1
    if n % 2:
        return 1 + map_collatz_helper(3*n+1, f)
    return 1 + map_collatz_helper(n/2, f)


def map_collatz(n, f):
    return map_collatz_helper(n, f)


def f1(k):
    print((k+1)/0.25)


# ans = map_collatz(6, f1)

# print(ans)

def guess_pass_helper(pwd, text, pwd_idx, text_idx, curr):
    if pwd_idx == len(pwd):
        return curr
    if text_idx == len(text):
        return False
    pwd_val = pwd[pwd_idx]
    text_val = text[text_idx]
    if pwd_val == text_val:
        return guess_pass_helper(pwd, text, pwd_idx+1, text_idx+1, curr+[text_idx])
    return guess_pass_helper(pwd, text, pwd_idx, text_idx+1, curr)


def guess_pass(pwd, text):
    return guess_pass_helper(pwd, text, 0, 0, [])


pwd = "abc-123"
text = "a1b2c34/-1x2gh3n"
# print(
#     guess_pass(pwd, text)

# )


def n_of_sums_helper(n, start, fun, curr):
    next_val = fun(start)
    if curr == n:
        return 1
    if start <= 0:
        return 0
    return n_of_sums_helper(n, next_val, fun, curr+start) + n_of_sums_helper(n, next_val, fun, curr)


def n_of_sums(n, k, fun):
    return n_of_sums_helper(n, k, fun, 0)


# print(
#     n_of_sums(12, 12, lambda b: b-2)
# )

def all_sums_helper(num, bound, prev, curr, summ):
    if summ > num:
        return
    if summ == num:
        yield curr
        return
    for i in range(1, bound+1):
        if not prev or i <= prev:
            yield from all_sums_helper(num, bound, i,
                                       f"{i}" if not curr else curr+f" + {i}", summ+i)


def all_sums(num, bound):
    yield from all_sums_helper(num, bound, None, "", 0)


res = all_sums(4, 4)
# print(
#     list(res)


# )

def f3_helper(n, x, y, curr, arr):
    if len(curr) == n:
        arr.append(curr)
        return

    if not curr:
        f3_helper(n, x, y, curr+[x], arr)
        f3_helper(n, x, y, curr+[y], arr)
    else:
        f3_helper(n, x, y, curr+[x], arr)
        if curr[-1] is not y:
            f3_helper(n, x, y, curr+[y], arr)


def f3(n, x, y):
    arr = []
    f3_helper(n, x, y,  [], arr)
    print(arr)
    return arr


# f3(3, 'a', (2,))

def rotate_90_clock(mat):
    return list(map(lambda x: list(x)[::-1], zip(* mat)))


mat = [[1, 2], [3, 4], [5, 6]]
# print(
#     rotate_90_clock(mat)


# )
y = [z for x in mat for z in x]
# print(y)


def sink_nodes_helper(root):
    data, right, left = root.data, root.right, root.left
    if left:
        if left.data:
            root.data = left.data
            left.data = data
            sink_nodes_helper(left)
            return
    if right:
        if right.data:
            root.data = right.data
            right.data = data
            sink_nodes_helper(right)
            return


def sink_nodes(root):
    if not root:
        return
    sink_nodes(root.left)
    sink_nodes(root.right)
    if root.data == 0:
        sink_nodes_helper(root)
    return root


class Node:
    def __init__(self, data, left=None, right=None):
        self.left = left
        self.data = data
        self.right = right

    def __str__(self):
        return "(" + str(self.left or "") + " " + str(self.data) + " " + str(self.right or "") + ")"


root = Node(0, Node(0, Node(1)), Node(
    0, Node(0, Node(6), Node(4)), Node(2, Node(3))))


def print_tree(root, val="data", left="left", right="right"):
    def display(root, val=val, left=left, right=right):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if getattr(root, right) is None and getattr(root, left) is None:
            line = '%s' % getattr(root, val)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if getattr(root, right) is None:
            lines, n, p, x = display(getattr(root, left))
            s = '%s' % getattr(root, val)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if getattr(root, left) is None:
            lines, n, p, x = display(getattr(root, right))
            s = '%s' % getattr(root, val)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = display(getattr(root, left))
        right, m, q, y = display(getattr(root, right))
        s = '%s' % getattr(root, val)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * \
            '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + \
            (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + \
            [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    lines, *_ = display(root, val, left, right)
    for line in lines:
        print(line)


# print_tree(root)
# sink_nodes(root)
# print_tree(root)
d = {
    "n": 0,
    "m": 0
}


def rec_iter(x):
    d["n"] += 1
    if x == 1:
        yield x
        return
    for i in rec_iter(x-1):
        yield i
    yield x


def rec_iter2(x):
    d["m"] += 1
    if x == 1:
        yield x
        return
    for i in rec_iter2(x-1):
        yield i
    yield x


n = 3
# m = 2
# for i in rec_iter(n):
#     for j in rec_iter2(m):
#         pass
# print(d)


def zort2(lst):
    for a in range(len(lst)-1):
        for b in range(1, len(lst)):
            if lst[a] < lst[b]:
                lst[a], lst[b] = lst[b], lst[a]


# lst = [2,1]

# zort2(lst)
# print(lst)
def inter_helper(intervals, curr, lest):
    best = 0
    if not intervals:
        return len(curr)
    popped = intervals.pop()
    print(curr, lest, popped)

    x, y = popped
    if not lest:
        best = max(best, inter_helper(
            intervals, curr+[popped], (x, y)))
    elif x > lest[0] and x < lest[1]:
        best = max(best, inter_helper(
            intervals, curr+[popped], (x, min(lest[1], y))))
    best = max(best, inter_helper(intervals, curr, lest))
    intervals.append(popped)
    return best


def inter(intervals):
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[0], reverse=True)
    return inter_helper(intervals, [], None)
    # best = 1
    # low, high = intervals[0]
    # prev_low, prev_high = intervals[0]
    # for x, y in intervals[1:]:
    #     if x > low and y < high:
    #         prev_low, prev_high = low, high
    #         best += 1
    #         low, high = x, y
    #     else:
    #         if y < high:
    #             continue

    return best


intvals = [(3, 8), (2, 4), (4, 5), (0, 5), (2, 7), (1, 8), (4.1, 4.8)]
# print(
#     inter(intvals)

# )
x = [0] * 3
print('id(x)', id(x))  # address of list x
print('\nid(x[0])', id(x[0]))  # address of 0, the 1st element of x
print('id(x[1])', id(x[1]))
print('id(x[2])', id(x[2]))
# try with variables
a = 0
b = 0
c = 0
d_zeros = [a, b, c]
print('\nid(d_zeros)', id(d_zeros))  # address of list d
# address of 1000, the 1st element of d
print('\nid(d_zeros[0])', id(d_zeros[0]))
print('id(d_zeros[1])', id(d_zeros[1]))
print('id(d_zeros[2])', id(d_zeros[2]))


class Bicycle:  # Bicycle is a new type of objects
    """Have a nice ride"""
    pass


def quick(lst):
    if not lst:
        return []
    pivot = random.randint(0, len(lst)-1)
    pivot_val = lst[pivot]
    greater = []
    lesser = []
    for i, elm in enumerate(lst):
        if i == pivot:
            continue
        if elm >= pivot_val:
            greater.append(elm)
        else:
            lesser.append(elm)
    return quick(lesser)+[pivot_val]+quick(greater)


p = [3, 2, 5, 1]
print(
    quick(p)

)


       