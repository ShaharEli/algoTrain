

# def sum_non_adj(lst):
#     if not lst:
#         return 0
#     return max([lst[0]+sum_non_adj(lst[2:]), sum_non_adj(lst[1:])])


# print(sum_non_adj([1, 2, 3, 4]))
# print(sum_non_adj([2, 21, 8, 2, 5, 3]))
# print(sum_non_adj([10, 1, 2, 3, 4, 11, 2, 6]))

# print(sum_non_adj([2, 3, 4, -5]))


def sum_non_adj(lst):
    if not lst:
        return 0
    return max(lst[0]+sum_non_adj(lst[2:]), sum_non_adj(lst[1:]))


# print(sum_non_adj([1, 2, 3, 4]))
# print(sum_non_adj([2, 21, 8, 2, 5, 3]))
# print(sum_non_adj([10, 1, 2, 3, 4, 11, 2, 6]))

# print(sum_non_adj([2, 3, 4, -5]))


def tree_leavs_helper(lst, curr, end):
    next_left = (2*curr)+1
    next_right = (2*curr)+2
    if next_left >= end:
        yield lst[curr]
        return
    if next_left < end and lst[next_left] is not None:
        yield from tree_leavs_helper(lst, next_left, end)
    if next_right < end and lst[next_right] is not None:
        yield from tree_leavs_helper(lst, next_right, end)


def tree_leavs(bin_lst):
    yield from tree_leavs_helper(bin_lst, 0, len(bin_lst))


# ls = [7, 3, 9, 1, 4, 8, None, None, 2]

# for i in tree_leavs(ls):
    # print(i)


def sub_lsts_helper(lst, curr, all_subs):
    if not lst:
        all_subs.append(curr)
        return
    popped = lst.pop()
    sub_lsts_helper(lst, curr, all_subs)
    sub_lsts_helper(lst, [popped] + curr, all_subs)
    lst.append(popped)


def sub_lsts():
    n = 0
    while True:
        arr = []
        sub_lsts_helper([x+1 for x in range(n)], [], arr)
        yield arr
        n += 1


# lala = sub_lsts()
# print(next(lala))
# print(next(lala))
# print(next(lala))
# print(next(lala))
class Tree:
    def __init__(self, value, branches=[]):
        self.value = value
        self.branches = list(branches)


def bfs_order_helper(tree, start, end):
    if not tree:
        return
    value, branches = tree.value, tree.branches
    yield value
    for branch in branches:
        yield from bfs_order(branch)


def bfs_order(tree):
    if not tree:
        return
    value, branches = tree.value, tree.branches
    yield value
    while True:
        new_brunches = []
        for branch in branches:
            value, branches = branch.value, branch.branches
            yield value
            new_brunches.extend(branches)
        branches = new_brunches
        if not branches:
            return


# print(list(bfs_order(
#     Tree(1, [Tree(2, [Tree(5), Tree(6)]), Tree(3, [Tree(7)]), Tree(4, [Tree(8)])]))))
class Node:
    def __init__(self, data, next=None):
        self.data, self.next = data, next


def eq_sums(L1, L2):
    runner_l1 = L1
    prev_l1 = None
    sum_l1 = 0
    while runner_l1:
        sum_l1 += runner_l1.data
        prev_l1 = runner_l1
        runner_l1 = runner_l1.next
    runner_l2 = L2
    prev_l2 = None
    sum_l2 = 0
    while runner_l2:

        sum_l2 += runner_l2.data
        prev_l2 = runner_l2
        runner_l2 = runner_l2.next
    if sum_l1 > sum_l2:
        diff = sum_l1 - sum_l2
        start = prev_l2
        head = L2
    else:
        diff = sum_l2 - sum_l1
        start = prev_l1
        head = L1
    while diff:
        start.next = Node(1)
        start = start.next
        diff -= 1

    return head


L1 = Node(5, Node(-3, Node(8, Node(1, Node(5)))))
L2 = Node(7, Node(1, Node(2, Node(3, Node(6)))))


def printo(x):
    curr = x
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print()


dd = eq_sums(L1, L2)
printo(dd)
