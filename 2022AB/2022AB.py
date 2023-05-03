def xyz_helper(s, curr, sett, max_len):
    if len(curr) == max_len:
        sett.add("".join(curr))
        return
    for i, elm in enumerate(s):
        curr.append(elm)
        s.pop(i)
        if i == 0:
            xyz_helper(s, curr, sett, max_len)
        else:
            xyz_helper(s, curr, sett, max_len)
        s.insert(i, elm)
        curr.pop()


def xyz(num_x, num_y, num_z):
    sett = set()
    xyz_helper(list(num_x*"x"+num_y*"y"+num_z*"z"),
               [], sett, num_x+num_y+num_z)
    return list(sett)

# def xyz_helper(num_x, num_y, num_z, curr, arr):
#     if sum([num_x, num_y, num_z]) == 0:
#         arr.append(curr)
#         return
#     if num_x > 0:
#         xyz_helper(num_x-1, num_y, num_z, curr+"x", arr)
#     if num_y > 0:
#         xyz_helper(num_x, num_y-1, num_z, curr+"y", arr)
#     if num_z > 0:
#         xyz_helper(num_x, num_y, num_z-1, curr+"z", arr)


# def xyz(num_x, num_y, num_z):
#     arr = []
#     xyz_helper(num_x, num_y, num_z,
#                "", arr)
#     return arr


print(xyz(2, 0, 1))


def get_k_tuples(it, k):
    curr = next(it)
    ls = []
    stop = False
    while curr:
        while len(ls) < k:
            ls.append(curr)
            try:
                curr = next(it)
            except:
                stop = True
                break

        if len(ls) == k:
            yield tuple(ls)
        if stop:
            break
        ls = ls[1:]

    # while i<k:
# print(next(get_k_tuples(iter([1, 2, 3, 4, 5]), 6)), end="")


class Node:
    def __init__(self, data, next=None):
        self.data, self.next = data, next


def find_max_pair(head):
    if not head.next:
        return head.data
    maxx = None
    curr = head
    runner = curr
    end = None
    prev = None
    if not end:
        while runner.next:
            prev = runner
            runner = runner.next
        end = runner
    maxx = end.data+head.data
    while True:
        curr = curr.next
        if curr == prev:
            return max(maxx, curr.data+prev.data)
        runner = curr
        while runner.next != end:
            prev = runner
            runner = runner.next
        end = runner
        maxx = max(end.data+curr.data, maxx)
        if prev == curr:
            return max(maxx, curr.data)


# def intersect(intervals, points):
#     if not intervals or not points:
#         return False
#     setted_points = set(points)
#     setted_intervals = set(intervals)
#     while len(setted_points):
#         top_bound = max(intervals, key=lambda x: x[1])
#         bottom_bound = min(intervals, key=lambda x: x[0])

#         for point in setted_points:
#             if point ==
#             if point < bottom_bound:
#                 setted_points.remove(point)
#             if point > top_bound:


# intersect([(1, 2), (3, 4)], [1])


class Node:
    def __init__(self, data, children):
        self.data, self.children = data, children


def check_tree_helper(root, curr):
    children = root.children
    if not children:
        return curr % 2
    children_data = [check_tree_helper(child, curr+1) for child in children]
    if all(children_data):
        return 1
    if children_data.count(0) == len(children_data):
        return 0
    return None


def check_tree(root):
    return check_tree_helper(root, 0)


def uncurry(amount_of_args):
    def decorator(f):
        def wrapper(*v):
            if len(v) != amount_of_args:
                raise TypeError
            if not v:
                return f()
            g = f
            for elm in v:
                g = g(elm)
            return g
        return wrapper
    return decorator


@uncurry(3)
def f(x):
    return lambda y: lambda z: x+y+z


# print(
    # f(1, 2, 3)
# )
# new = {v: [k for k in d.keys() if d[k] == v] for v in d.values()}

# lst = Node(7, Node(1, Node(2, Node(4, Node(-3, Node(-2))))))


def in_interval(interval, point):
    x, y = interval
    return x <= point <= y


def intersect(intervals, points):
    if not intervals or not points:
        return False
    intervals.sort(key=lambda x: x[0])
    points.sort()
    while intervals and points:
        end_point = points[-1]
        end_interval = intervals[-1]
        if in_interval(end_interval, end_point):
            return True
        if end_point > end_interval[1]:
            points.pop()
        else:
            intervals.pop()
    return False



def get_k_tup(itr):
    val = True
    while val:
        val=next(itr,False)