class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def tree_iter_helper(root, target):
    if target == 0:
        yield root.data
        return
    left, right = root.left, root.right
    if left:
        yield from tree_iter_helper(left, target-1)
    if right:
        yield from tree_iter_helper(right, target-1)


def tree_iter(root, depth):
    for i in range(depth):
        yield from tree_iter_helper(root, i)


root = Node(1, Node("A", Node("2")), Node(
    "B", Node("3", Node("c")), Node("4")))
# for i in tree_iter(root, 3):
# print(i)


def unify(lst):
    i = 0
    while i < len(lst):
        lst.sort(key=lambda x: x[0])
        tail = lst[i]
        to_remove = []
        for x, y in lst[i + 1:]:
            print(tail, lst)
            if x <= tail[1]:
                to_remove.append((x, y))
                tail = (tail[0], y)
        lst[i] = tail
        for elm in to_remove:
            lst.remove(elm)
        i += 1
    return lst


# print(
#     unify([
#         (2.2, 5),
#         (1, 4.2),
#         (7.1, 9)
#     ])
# )

def is_legal_BST_helper(root, less_than, greater_than):
    if not root:
        return True
    data = root.data
    right, left = node.right, node.left
    if less_than is not None:
        if less_than <= data:
            return False
        if greater_than >= data:
            return False

    return is_legal_BST_helper(right, less_than, root.data) and is_legal_BST_helper(left, root.data, greater_than)


def is_legal_BST(root):
    return is_legal_BST_helper(root, None, None)


def min_time_helper(workers_hours, tasks, end):
    curr_sum = sum(workers_hours)
    if curr_sum == end:
        return max(workers_hours)
    curr_task = tasks.pop()
    minn = end
    for worker_idx in range(len(workers_hours)):
        workers_hours[worker_idx] += curr_task
        minn = min(min_time_helper(workers_hours, tasks, end), minn)
        workers_hours[worker_idx] -= curr_task
    tasks.append(curr_task)
    return minn


def min_time(num_workers, tasks):
    return min_time_helper([0 for _ in range(num_workers)], tasks, sum(tasks))


# print(min_time(5, [4, 2, 2.5, 2, 3, 5]))
class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class Cycle:
    def __init__(self, data):
        self.data = data
        self.curr = Node(data)
        self.curr.next = self.curr
        self.curr.prev = self.curr

    def rotate(self):
        self.curr = self.curr.next
        return self.curr.data

    def rotate_back(self):
        self.curr = self.curr.prev
        return self.curr.data

    def insert_next(self, data):
        curr_next = self.curr.next
        next = Node(data, self.curr, self.curr.next)
        self.curr.next = next
        curr_next.prev = next

    def delete(self):
        if self.curr == self.curr.next:
            raise LookupError
        next = self.curr.next
        prev = self.curr.prev
        prev.next = next
        next.prev = prev
        self.curr = next


# cycle = Cycle(3)
# cycle.insert_next(2)
# cycle.insert_next(1)
# print(cycle.rotate())
# print(cycle.rotate())
# print(cycle.rotate())
# print(cycle.rotate())
# cycle.delete()
# print(cycle.rotate_back())
# def fix(d):

#     def decorator(func):
#         def wrapper(v):

#         return wrapper
#     return decorator


def fix(d):
    sorted_keys = sorted(d.keys())

    def decorator(func):
        def wrapper(*v):
            v = list(v)
            for key in sorted_keys:
                v.insert(key, d[key])
            return func(*v)

        return wrapper
    return decorator


@ fix({3: "2", 2: "c", 0: "a"})
def g(x, y, z, t):
    return x + y + z+t


# print(g("b"))
def unified(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    low, high = intervals[0][0], intervals[0][1]
    new_lst = []
    for x, y in intervals:
        if x <= high and y >= high:
            high = y
        elif x >= low and y <= high:
            continue
        else:
            new_lst.append((low, high))
            low = x
            high = y
    new_lst.append((low, high))
    return new_lst


string = "abc"


def hi(string):
    x = [(i, string[i]) for i in range(len(string))]
    while x:
        yield x.pop()


for x in hi(string):
    print(x)
