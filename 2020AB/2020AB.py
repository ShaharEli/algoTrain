
from functools import reduce


def count_substrs(string):
    summ = 0
    if not string:
        return summ
    tail = string[0]
    rest = string[1:]
    summ += 1 + rest.count(tail) + count_substrs(rest)
    return summ


# print(count_substrs("abaacb"))


def appear_at_least(word_list, k):
    return set(filter(lambda y: reduce(lambda curr, x: curr + (1 if x == y else 0), word_list, 0) >= k, word_list))


# print(appear_at_least(["a", "b", "c", "a", "b", "b", "d"], 2))


def go_over_in_order(iterable):
    min = None
    curr = None
    while True:
        curr = None
        if not min:
            for val in iterable:
                if min is None:
                    min = val
                if val < min:
                    min = val
            yield min
            continue
        else:
            for val in iterable:
                if curr is None and val > min:
                    curr = val
                elif curr is not None and curr > val > min:
                    curr = val

        if not curr:
            return
        min = curr
        yield min


# ls = [10, 2, 7, 3]
# hi = go_over_in_order(ls)
# print(next(hi))
# print(next(hi))
# print(next(hi))
# print(next(hi))
# print(next(hi))
class Node:
    def __init__(self, data, next=None):
        self.data, self.next = data, next


def shift(x, k):
    t = 0
    curr = x
    while t < k:
        prev = curr
        curr = curr.next
        t += 1
    prev.next = None
    temp = curr
    while curr.next:
        curr = curr.next
    curr.next = x
    return temp


# lnk = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
# l1 = shift(lnk, 3)
# curr = l1
# while curr:
#     print(curr.data)
#     curr = curr.next
# def min_chars_helper(s1, s2):
#     pass


# def min_chars(s1, s2):
#     if s1 in s2:
#         return 0
#     if not s2 and s1:
#         return None
#     min = None
#     i = 0
#     while i < len(s1):
#         tail = s1[i]
#         rest = s1[i+1:]
#         sliced_s2 = s2[i+1:]
#         print(sliced_s2)
#         checker = min_chars(rest, sliced_s2)
#         if checker is not None:
#             if not min:
#                 min = checker+1
#             if checker + 1 < min:
#                 min = checker + 1
#         for i, n in enumerate(sliced_s2):
#             if n == tail:
#                 checker2 = min_chars(rest, sliced_s2)
#                 if checker2 is not None:
#                     if not min:
#                         min = checker2+1
#                     if checker + 1 < min:
#                         min = checker2 + 1
#         i += 1
#     return min

# def min_chars(s1, s2):


def min_chars(s1, s2):
    min_ans = len(s1)
    for i in range(len(s2) - len(s1)+1):
        new_min = 0
        for j in range(len(s1)):
            if s1[j] != s2[j+i]:
                new_min += 1
        min_ans = min(min_ans, new_min)

    return min_ans
    # def min_chars(s1, s2):


print(
    min_chars("cdef", "abzdef"),
    min_chars("abc", "azbzc"),
    min_chars("abc", "pdxzk"),

)
