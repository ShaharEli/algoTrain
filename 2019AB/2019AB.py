class Node:
    def __init__(self, data, left=None, right=None):
        self.data, self.left, self.right = data, left, right


def scramble_helper(root, level, arr):
    if not root:
        return
    data, left, right = root.data, root.left, root.right

    if not left and not right:
        arr.append(data)
        return
    if level % 2 == 1:
        root.left, root.right = root.right, root.left
    scramble_helper(left, level+1, arr)
    scramble_helper(right, level+1, arr)


def scramble(root):
    arr = []
    scramble_helper(root, 0, arr)
    return arr


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
            '' + s + y * '' + (m - y) * ' '
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


# tree = Node(1, Node(2, Node(4), Node(5, Node(7))), Node(3, Node(6)))
# print_tree(tree)
# print(
#     scramble(tree)

# )
# print_tree(tree)
def ranksearch_helper(lst, k):
    minimal = min(lst)
    if k == 1:
        return minimal
    lst.remove(minimal)
    return ranksearch_helper(lst, k-1)


def quicksort(lst):
    if not lst:
        return []
    midd = len(lst)//2
    greater = []
    smaller = []
    curr = lst[midd]
    for idx, elm in enumerate(lst):
        if idx == midd:
            continue
        if elm >= curr:
            greater.append(elm)
        else:
            smaller.append(elm)
    return quicksort(smaller) + [curr] + quicksort(greater)


def ranksearch(lst, k):

    copy = lst[:]
    new_lst = quicksort(copy)
    return new_lst[k-1]


# print(ranksearch([3, 2, 7, 9, 1], 4))

def longest_chain(dict1):
    checked = dict()
    maxx = 1
    counted = 0
    for key in dict1:
        if counted == len(dict1):
            break
        curr = key
        count = 0
        history = []
        while curr:
            history.append(curr)
            count += 1
            curr = dict1.get(curr, None)
            if not curr:
                break
            if curr in checked:
                count += checked[curr]
                break
        counted += count
        for i in range(len(history)):
            checked[history[i]] = count-i
        maxx = max(count, maxx)
    return maxx


dict1 = {
    "1": "2",
    "3": "4",
    "6": "2",
    "3": "2",
    "1": "2",
    "1": "2",
}
# print(longest_chain(dict1))


class DropWhile:
    def __init__(self, f, it):
        self.f = f
        self.it = it
        self.checked = False

    def __iter__(self):
        return self

    def __next__(self):
        next_val = next(self.it)
        if self.checked:
            return next_val
        if not self.f(next_val):
            self.checked = True
            return next_val
        return next(self)


def f(x): return x < 3


i = iter([1, 2, 3, 4, 5, 6, 0, 1])
lst = list(DropWhile(f, i))
print(lst)
