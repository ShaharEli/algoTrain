from this import s


def eq_vals(func, lzt):
    res = dict()
    for item in lzt:
        result = func(item)
        res[result] = res.get(result, [])+[item]

    return list(res.values())


lzt = list(range(1, 14))
def func(x): return (x % 3)*2 - x % 2


# print(
#     eq_vals(func, lzt)

# )


def edit_distance_helper(curr, target, steps, idx):
    if len(curr) > len(target):
        return len(target)
    if curr == target:
        return steps
    if idx > len(curr)-1:
        return steps + len(target)-len(curr)
    curr_data = curr[idx]
    target_data = target[idx]
    if curr_data == target_data:
        return edit_distance_helper(curr, target, steps, idx+1)
    insert_checker = edit_distance_helper(
        curr[:idx]+target_data + curr[idx:], target, steps+1, idx+1)
    replace_checker = edit_distance_helper("".join(
        [target_data if i == idx else x for i, x in enumerate(curr)]), target, steps+1, idx+1)
    return min(insert_checker, replace_checker)


def edit_distance(a, b):
    if len(a) > len(b):
        return edit_distance_helper(b, a, 0, 0)
    return edit_distance_helper(a, b, 0, 0)


# print(edit_distance("abc", "bc"))
# print(
#     edit_distance("abc", "cde")

# )

# print(
#     edit_distance("axbyc", "abc")

# )

# print(
#     edit_distance("abc", "abc")

# )
class Node:
    def __init__(self, data, next=None):
        self.data, self.next = data, next

    def __repr__(self):
        return repr(self.data) + "->" + repr(self.next)


def split(head, k):
    heads = []
    curr = head
    c = 0
    while curr:
        if c % k == 0:
            heads.append(curr)
            next = curr.next
            curr.next = next
            curr = next
        else:
            curr = curr.next
        c += 1
    return heads


# lst = Node(5, Node(-3, Node(8, Node(1, Node(5)))))
# print(split(lst, 2))  # [5->-3->None, 8->1->None, 5->None]
# lst2 = Node(1, Node(7, Node(2)))
# print(split(lst2, 1))  # [1->None, 7->None, 2->None]
# lst3 = Node(2, Node(2, Node(9)))
# print(split(lst3, 3))  # [2->2->9->None]

def get_max(table, row, start, curr):
    if row == len(table):
        return curr
    maxx = None
    if row == 0:
        for i in range(len(table[row])):
            res = get_max(table, row+1, i, curr+table[row][i])
            if maxx is None:
                maxx = res
            else:
                maxx = max(maxx, res)
    else:
        maxx = max(
            get_max(table, row+1, start, curr+table[row][start]),
            get_max(table, row+1, start+1, curr+table[row][start+1])
        )
    return maxx


def opti_sum(table):
    for i in range(len(table)):
        yield get_max(table[:i+1], 0, 0, 0)


table = [[4, 2, 3],
         [2, 3, 4, 1, 6],
         [3, 4, 1, 5, 9, 4, 3]]
g = opti_sum(table)

for i in g:
    print(i)
