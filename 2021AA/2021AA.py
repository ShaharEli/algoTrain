vec = [0, 0, 6, 0, 3, 6]


def tranduce(vec):
    sp = {val: key for val, key in enumerate(vec) if key}
    return sp


def combination_lock(*args):
    d = {
        "curr": 0,
        "end": len(args)-1,
        "args": args,
        "checker": True,
    }

    def f(v):
        if v != d["args"][d["curr"]]:
            d["checker"] = False
        if d["curr"] == d["end"]:
            checker = d["checker"]
            d["checker"] = True
            d["curr"] = 0
            return checker
        else:
            d["curr"] += 1
            return f
    return f


# f = combination_lock(1, 2, 3, 4)
# print(f(1)(2)(3)(4))
# print(f(1)(1)(1)(1))
# print(f(4)(3)(2)(1))
# g = combination_lock(1, 2)
# print(
#     g(1)(2)
# )

# print(
#     g(7)(8)
# )
# print(
#     g(2)(1)
# )
def find_range(dict_list):
    keys_set = set()
    range_dict = {}
    for dictionary in dict_list:
        for k, v in dictionary.items():
            prev_val = range_dict.get(k)
            if not prev_val:
                range_dict[k] = [v, v]
            else:
                x, y = prev_val
                range_dict[k] = [min(v, x), max(v, y)]
            keys_set.add(k)
    sorted_keys = sorted(keys_set)
    return range_dict, sorted_keys


dict_list = [{"glop": 4, "is": 7, "best": 10}, {
    "glop": 2, "best": 6}, {"glop": 1, "is": 2}, {"dippy": 2}]
# print(
# find_range(dict_list)
# )


# def sink_nodes_helper(root):
#     if not root:
#         return False
#     data, left, right = root.data, root.left, root.right
#     checker = False
#     if left:
#         left_data = left.data
#         if not data and left_data:
#             root.data = left_data
#             left.data = 0
#             checker = True
#     if right:
#         data = root.data
#         right_data = right.data
#         if not data and right_data:
#             root.data = right_data
#             right.data = 0
#             checker = True

#     return checker or sink_nodes_helper(left) or sink_nodes_helper(right)


# def sink_nodes(root):
#     while sink_nodes_helper(root):
#         print_tree(root)
#         pass
#     return root
def sink_nodes_helper(root, prev):
    data, left, right = root.data, root.left, root.right
    if not left and not right:
        if not prev:
            return
        if data and not prev.data:
            root.data = 0
            prev.data = root.data
        return
    if left:
        left_data = left.data
        if not root.data and left_data:
            root.data = left_data
            left.data = 0
        sink_nodes_helper(left, root)
        left_data = left.data
        if not root.data and left_data:
            root.data = left_data
            left.data = 0
            sink_nodes_helper(left, root)

    if right:
        data = root.data
        right_data = right.data
        if not data and right_data:
            root.data = right_data
            right.data = 0
        sink_nodes_helper(right, root)
        data = root.data
        right_data = right.data
        if not data and right_data:
            root.data = right_data
            right.data = 0
            sink_nodes_helper(right, root)


def sink_nodes(root):
    sink_nodes_helper(root, None)


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
def f(start, end, step):
    print(start, end=" ")
    if start < end:
        f(start+step, end, step)
        print(start, end=" ")


# f(1, 12, 3)
def multi_range_helper(lst, starter):
    if len(lst)-1 == starter:
        return
    start = lst[starter]
    end = lst[starter+1]
    if start < end:
        yield from range(start, end)
    elif start > end:
        yield from range(start, end, -1)
    yield from multi_range_helper(lst, starter+1)


def multi_range(lst):
    if not lst or len(lst) == 1:
        return
    yield from multi_range_helper(lst, 0)


# print(*multi_range([1, 3, -1, 4, 4, 7]))
# print(*multi_range([1]))

class MyKeyError(Exception):
    pass


class MultiSet:
    def __init__(self):
        self.__data = dict()

    def __get_vals_arr(self):
        arr = []
        for k, v in self.__data.items():
            arr += [k]*v
        return arr

    def __str__(self):
        string = "{"
        start = True
        for k, v in self.__data.items():
            for i in range(v):
                if not start:
                    string += ", "
                start = False
                string += str(k)
        string += "}"
        return string

    def insert(self, val):
        prev = self.__data.get(val)
        if prev is not None:
            self.__data[val] += 1
        else:
            self.__data[val] = 1

    def extend(self, vals):
        for val in vals:
            self.insert(val)

    def remove(self, val):
        if not self.__data.get(val):
            raise MyKeyError
        else:
            self.__data[val] -= 1

    def __iter__(self):
        return (val for val in self.__get_vals_arr())


m = MultiSet()
m.insert("a")
m.insert("a")
m.insert("b")
m.insert("b")
m.remove("b")
m.insert("c")
m.extend([1, 2, 3])
print(m)
hi = iter(m)


def flip(lst, i):
    for j in range((i+1)//2):
        lst[i - j], lst[j] = lst[j], lst[i-j]


def pancake_sort(lst):
    if not lst:
        return []
    maxx = lst[0]
    maxx_idx = 0
    end = len(lst)
    while end-1:
        for i in range(1, end):
            if lst[i] > maxx:
                maxx = lst[i]
                maxx_idx = i
        if not maxx_idx:
            print(f"flipping {end-1}")
            flip(lst, end-1)
        else:
            if end-1 != maxx_idx:
                print(f"flipping {maxx_idx}")
                flip(lst, maxx_idx)
                print(f"flipping {end-1}")
                flip(lst, end-1)

        end -= 1
        maxx = lst[0]
        maxx_idx = 0


lst = [2, 1, 4, 3, 5]
pancake_sort(lst)
print(lst)

# def pancake_sort(lst):
