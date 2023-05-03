
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def linked_filter(f, lnk):
    new_head = None
    curr_node = None
    curr = lnk
    while curr:
        if f(curr.data):
            new_node = Node(curr.data)
            if not new_head:
                new_head = new_node
                curr_node = new_head
            else:
                curr_node.next = new_node
                curr_node = curr_node.next
        curr = curr.next
    return new_head


# hi = linked_filter(lambda x: (x+1) %
#                    2, Node(2, Node(3, Node(4, Node(5, Node(6))))))
# print(hi.next.next.data)


def all_sums_helper(num, opts, curr):
    if sum(curr) == num and sorted(curr, reverse=True) != curr:
        return
    if sum(curr) == num:
        yield " + ".join(map(lambda x: str(x), curr))
    if sum(curr) > num:
        return
    for opt in opts:
        curr.append(opt)
        yield from all_sums_helper(num, opts, curr)
        curr.pop()


def all_sums(num, bound):
    opts = list(range(1, bound+1))
    yield from all_sums_helper(num, opts, [])


# res = all_sums(4, 3)
# print(list(res))


def f3_helper(n, x, y, curr, arr):
    if len(curr) == n:
        arr.append(curr[:])
        return
    curr.append(x)
    f3_helper(n, x, y, curr, arr)
    curr.pop()
    if not curr or curr[-1] != y:
        curr.append(y)
        f3_helper(n, x, y, curr, arr)
        curr.pop()


def f3(n, x, y):
    arr = []
    f3_helper(n, x, y, [], arr)
    return arr


# print(
    # f3(3, 'a', (2,))
# )


def f4_helper(st, dict1, k, curr, arr, start, row):
    if row == k:
        return
    if len(curr) == k:
        arr.append(curr[:])
        return
    if start == len(st):
        return
    f4_helper(st, dict1, k, curr, arr, start+1, 0)
    curr.append(st[start])
    f4_helper(st, dict1, k, curr, arr, start + 1, row + 1)
    curr.pop()


def f4(st, dict1, k):
    arr = []
    f4_helper(st, dict1, k, [], arr, 0, 0)
    return max(arr, key=(lambda x: sum([dict1[lett] for lett in x])))


# print(
#     f4("abzzcd", {
#         "a": 1,
#         "b": 1,
#         "c": 1,
#         "d": 1,
#         "m": 1,
#         "n": -1,
#         "e": -1,
#         "z": -1
#     }, 4)
# )

def rotate_90_clock(mat):
    mat.reverse()
    new_mat = [
        [0 for __ in range(len(mat))] for _ in range(len(mat[0]))
    ]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            new_mat[j][i] = mat[i][j]

    mat = new_mat


# hi = [
#     [1, 2],
#     [3, 4],
#     [5, 6]
# ]
# rotate_90_clock(hi)


class Campus:
    def __init__(self):
        self.__dict = {}

    def add_classmate(self, st1, st2):
        if not self.__dict.get(st1):
            self.__dict[st1] = set()
        if not self.__dict.get(st2):
            self.__dict[st2] = set()
        self.__dict[st1].add(st2)
        self.__dict[st2].add(st1)

    def soc_dist(self, st1, st2, n):
        if not self.__dict.get(st1) or not self.__dict.get(st2):
            return False
        if st1 == st2:
            return True
        if n == 1:
            return st2 in self.__dict.get(st1)

        for student in self.__dict.get(st1):
            if self.soc_dist(student, st2, n-1):
                return True

        return False

    # def soc_dist(self, st1, st2, n):
    #     if not self.__dict.get(st1) or not self.__dict.get(st2):
    #         return False
    #     if n == 1:
    #         return st2 in self.__dict.get(st1)
    #     for st in self.__dict.get(st1):
    #         if self.soc_dist(st, st2, n-1):
    #             return True
    #     return False

    def get_dict(self):
        return self.__dict


teva = Campus()
teva.add_classmate('a', 'b')
teva.add_classmate('a', 'c')
teva.add_classmate('d', 'b')
teva.add_classmate('d', 'k')
# print(teva.get_dict())
# print("a-b", teva.soc_dist('a', 'b', 1))
# print("a-d", teva.soc_dist('a', 'd', 2))
# print("a-k", teva.soc_dist('a', 'k', 3))
# print("a-p", teva.soc_dist('a', 'p', 3))
# print("s-p", teva.soc_dist('s', 'p', 1))
# print("a-a", teva.soc_dist('a', 'a', 100))


def f5_helper(st, dict1, k, curr, start, row, arr):
    if row == k:
        return
    if len(curr) == k:
        arr.append(curr)
        return
    if start == len(st):
        return
    f5_helper(st, dict1, k, curr+st[start], start+1, row+1, arr)
    f5_helper(st, dict1, k, curr, start+1, 0, arr)


def f5(st, dict1, k):
    arr = []
    f5_helper(st, dict1, k, "", 0, 0, arr)
    return max(arr, key=lambda string: sum([dict1[letter] for letter in string]))


print(
    f5("abzcd", {
        "a": 1,
        "b": 1,
        "c": 1,
        "d": 1,
        "m": 1,
        "n": -1,
        "e": -1,
        "z": -1
    }, 4)
)
