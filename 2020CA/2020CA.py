import random


def seq_fib(n, t, k):
    if n < t-1:
        return 0
    if n == t-1:
        return k
    summ = 0
    for i in range(1, t+1):
        summ += seq_fib(n-i, t, k)
    return summ


def tree(root, subtrs=None):
    return [root, [] if subtrs is None else subtrs]


def root(tr):  # accepts a tree: tr
    return tr[0]


def subtrs(tr):  # accepts a tree: tr
    return tr[1]


def two_leves_helper(irgun, name, curr):
    root_node = root(irgun)
    childs = subtrs(irgun)
    if root_node == name:
        return curr
    if not childs:
        return None
    for child in childs:
        checker = two_leves_helper(child, name, [root_node] + curr)
        if checker:
            return checker
    return []


def two_levels(irgun, name):
    if not irgun:
        return[]
    found = two_leves_helper(irgun, name, [])
    while len(found) != 2:
        found.append(None)
    return found


irgun = tree('Iosi', [tree('Eti', [tree('Meni'), tree('Tal'), tree('Gil')]), tree(
    'Moshe', [tree('Eli'), tree('Nir'), tree('Avi')])])

two_levels(irgun, 'Eli')
two_levels(irgun, 'Gil')


def create_node(d):
    key, val = d
    return [key, val, [], []]


def get_left(node):
    return node[2]


def get_right(node):
    return node[3]


def get_key(node):
    return node[0]


def insert_bst(d, bst):
    if not bst:
        bst += create_node(d)
        return
    curr_key = get_key(bst)
    d_key = get_key(d)
    if curr_key > d_key:
        insert_bst(d, get_left(bst))
    else:
        insert_bst(d, get_right(bst))


def padd(arr1, arr2):
    while len(arr1) < len(arr2):
        arr1 = [0]+arr1
    return arr1


def go_digits(n, m):
    if not n and not m:
        return []
    n = padd(n, m)
    m = padd(m, n)
    return [sum(tup) for tup in list(zip(n, m))]
# print(

# go_digits([1,2,3],[])
#     )


# print(

# go_digits([1,2,3],[1,2])
#     )


def get_sum(schedule):
    summ = 0
    for classse in schedule:
        summ += classse[1][1]-classse[1][0]
    return summ


def check_if_valid_class(schedule, classs):
    for slot in schedule:
        if slot[-1] == classs[-1]:
            x1, y1 = slot[1]
            x2, y2 = classs[1]
            if x2 >= y1:
                continue
            if y2 <= x1:
                continue
            return False
    return True


def max_classes_helper(schedule, curr):
    if not schedule:
        return get_sum(curr)
    maxx = 0
    classs = schedule.pop()
    maxx = max(max_classes_helper(schedule, curr), maxx)

    if check_if_valid_class(curr, classs):
        curr.append(classs)
        maxx = max(max_classes_helper(schedule, curr), maxx)
        curr.pop()
    schedule.append(classs)
    return maxx


def max_classes(schedule):
    return max_classes_helper(schedule, [])


schedule = [("intro", [10, 14], "Sunday"),
            ("algebra", [10, 11], "Sunday"),
            ("OOP", [12, 15], "Monday"),
            ("cpp", [9, 12], "Monday"),
            ("statistics", [9, 11], "Monday")]

# print(max_classes(schedule))


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.length = 0


class IntroSet:
    def __init__(self):
        self.data_set = LinkedList()

    def add(self, num):
        curr = self.data_set.head
        while curr:
            if curr.data == num:
                return False
            curr = curr.next
        index = random.randint(0, self.data_set.length)
        curr = self.data_set.head
        new_node = Node(num)
        self.data_set.length += 1
        if index == 0:
            new_node.next = curr
            self.data_set.head = new_node
            return True
        runner = 0
        while runner < index-1:
            curr = curr.next
            runner += 1
        next = curr.next
        new_node.next = next
        curr.next = new_node
        return True

    def __repr__(self):
        string = "{"
        curr = self.data_set.head
        lst = []
        while curr:
            lst.append(str(curr.data))
            curr = curr.next
        string += ", ".join(lst)
        string += "}"
        return string

    def union(self, other):
        new_set = IntroSet()
        curr = self.data_set.head
        while curr:
            new_set.add(curr.data)
            curr = curr.next
        curr = other.data_set.head
        while curr:
            new_set.add(curr.data)
            curr = curr.next
        return new_set

    def my_intersection(self, other, func):
        new_set = IntroSet()
        curr = self.data_set.head
        while curr:
            curr_data = curr.data
            if func(curr_data):
                curr2 = other.data_set.head
                while curr2:
                    curr2_data = curr2.data
                    if curr2_data == curr_data:
                        new_set.add(curr_data)
                    curr2 = curr2.next
            curr = curr.next
        return new_set

    def __iter__(self):
        curr = self.data_set.head
        while curr:
            yield curr.data
            curr = curr.next


hi = IntroSet()
# hi.add(1)
# hi.add(2)
# hi.add(3)
# print(hi)
# vi = IntroSet()
# vi.add(3)
# vi.add(4)
# vi.add(5)
# print(vi)
# lsl = hi.union(vi)
# print(lsl)
