from tkinter import S


def make_closed_helper(dict1, start):
    if not dict1:
        return dict1
    keys = list(dict1.keys())
    if start >= len(dict1):
        return dict1

    start_key = keys[start]
    curr_key = keys[start]
    i = 0
    while dict1.get(curr_key, None) is not None:
        i += 1
        curr_key = dict1.get(curr_key)
        if curr_key == start_key:
            return make_closed_helper(dict1, start + i)
        if i > len(dict1) - start:
            if curr_key != start_key:
                del dict1[start_key]
                return make_closed_helper(dict1, start)
            return dict1
    del dict1[start_key]
    return make_closed_helper(dict1, start)


def make_closed(dict1):
    return make_closed_helper(dict1, 0)


# d = {1: 1,  2: 3, 4: 5, 5: 6,  6: 5, 7: 7}
# make_closed(d)
# print(d)

class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


def weave(a, b):
    zipped = list(zip(a, b))
    prev = None
    first = None
    for x, y in zipped:
        a_node = Node(x)
        if not first:
            first = a_node
        b_node = Node(y)
        a_node.prev = prev
        a_node.next = b_node
        b_node.prev = a_node
        if prev:
            prev.next = a_node
        prev = b_node
    return first


# lnk = weave([1, 7, 5], [2, 4, 3])
def has_x_peaks(lst, x):
    peaks_count = 0
    if len(lst) == 1:
        return x == 1
    if len(lst) == 2:
        if lst[0] == lst[1]:
            return 2 == x
        return 1 == x
    if lst[0] >= lst[1]:
        peaks_count += 1
    if lst[-1] >= lst[-2]:
        peaks_count += 1
    for i in range(1, len(lst)-1):
        prev = lst[i-1]
        curr = lst[i]
        next = lst[i+1]
        if curr >= prev and curr >= next:
            peaks_count += 1
    return peaks_count == x


# print(has_x_peaks([1, 3, 4, 4, 2, 8, 4, ], 4))


def find_valley_helper(lst, prev, curr, next_idx):
    if next_idx == len(lst):
        return curr
    prev_val = lst[prev]
    curr_val = lst[curr]
    next_val = lst[next_idx]
    if curr_val <= prev_val and curr_val <= next_val:
        return curr
    return find_valley_helper(lst, curr, next_idx, next_idx+1)


def find_valley(lst):
    return find_valley_helper(lst, 0, 0, 1)


# print(
#     find_valley([7, 5, 4, 3, 2, 7, 9, 10])

# )

def make_stack():
    stack = []

    def wrapper(*args):
        if not args:
            if stack:
                return stack.pop()
            return
        stack.append(args[0])

    return wrapper


s = make_stack()
# s(1)
# s(2)
# s(3)
# print(s())
# print(s(), s())
