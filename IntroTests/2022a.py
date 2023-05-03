from calendar import c
from itertools import cycle
from re import S

from pkg_resources import working_set


def unify(lst):
    copied_lst = lst[:]
    while True:
        copied_lst_copy = copied_lst[:]
        changed = False
        for tup1_idx, tup1 in enumerate(copied_lst_copy):
            if changed:
                break
            for tup2_idx, tup2 in enumerate(copied_lst_copy):
                if tup1_idx == tup2_idx:
                    continue
                x1, y1 = tup1
                x2, y2 = tup2
                if x1 <= x2 and y1 >= x2 and y2 >= y1:
                    copied_lst.pop(tup1_idx)
                    changed = True
                    break
        if not changed:
            return copied_lst


# print(
#     unify([
#         (2.2, 5),
#         (1, 4.2),
#         (7.1, 9)
#     ])
# )

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.right = right
        self.left = left


def is_legal_bts_helper(root, data):
    left = root.left
    right = root.right
    if not left and not right:
        return True
    if not right:
        if not left.data <= data:
            return False
        return is_legal_bts_helper(left, left.data)
    if not left:
        if not right.data >= data:
            return False
        return is_legal_bts_helper(right, right.data)
    if not left.data <= data or not right.data >= data:
        return False
    return is_legal_bts_helper(left, left.data) and is_legal_bts_helper(right, right.data)


def is_legal_bts(root):
    return is_legal_bts_helper(root, root.data)


# print(is_legal_bts(Node(3, Node(5), Node(7))))
# class Cycle:
#     def __init__(self, data):
#         self.data = [data]
#         self.curr_index = 0

#     def rotate(self):
#         self.curr_index += 1
#         if self.curr_index >= len(self.data):
#             self.curr_index = 0

#     def rotate_back(self):
#         self.curr_index += 1
#         if self.curr_index >= len(self.data):
#             self.curr_index = 0


def decorator(val):
    def decorator(function):
        def func(f):
            return val
        return func
    return decorator


@decorator(10)
def hi(x):
    return x + 1


@decorator(30)
def bi(x):
    return x * 10


def get_prev(_):
    prevs = [None]

    def prev(new_val):
        prev_data = prevs[-1]
        prevs.append(new_val)
        return prev_data
    return prev


@get_prev
def last_in():
    pass


class CycleNode:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class Cycle:
    def __init__(self, data=None):
        self.current = [CycleNode(data)]

    def get_current(self):
        return self.current[0]

    def __str__(self):
        current = self.get_current()
        string = ""
        while current.next:
            string += current.data + " => "
            current = current.next
        string += current.data
        return string

    def insert_next(self, data):
        current = self.get_current()
        next_node = CycleNode(data)
        temp_next = current.next
        next_node.prev = current
        current.next = next_node
        next_node.next = temp_next

    def rotate(self):
        current = self.get_current()
        if current.next:
            self.current = [current.next]
            return self.get_current().data
        else:
            prev = current
            while prev.prev:
                prev = prev.prev
            self.current = [prev]
            return prev.data

    def rotate_back(self):
        current = self.get_current()
        if current.prev:
            self.current = [self.current.prev]
            return self.get_current().data
        else:
            next = self.current
            while next.next:
                next = next.next
            self.current = [next]
            return self.get_current().data

    def delete(self):
        current = self.get_current()
        if not current.prev and not current.next:
            raise LookupError
        current = self.get_current()
        temp_next = current.next
        temp_prev = current.prev
        self.current = [temp_next]
        self.get_current().prev = temp_prev
        temp_prev.next = self.get_current()


def min_time_helper(num_workers, tasks, working_set, sum_tasks, lst):
    if sum(working_set) == sum_tasks:
        print(max(working_set))
        lst.append(working_set[:])
    if not tasks:
        return
    poped = tasks.pop()
    for i in range(num_workers):
        working_set[i] += poped
        min_time_helper(num_workers, tasks, working_set, sum_tasks, lst)
        working_set[i] -= poped
    tasks.append(poped)


def min_time(num_workers, tasks):
    working_set = [0 for _ in range(num_workers)]
    lst = []
    min_time_helper(num_workers, tasks, working_set, sum(tasks), lst)
    # print(lst)
    return min([max(ls) for ls in lst])
    # generate all sublists with len of tasks


lst = [4, 2, 2.5, 2, 3, 5]
print(sum(lst))
print(min_time(4, lst))
print(sum(lst))
