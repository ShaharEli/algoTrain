

class TreeNode:

    def __init__(self, value, left=None, right=None):
        self.__value = value
        self.__left = left
        self.__right = right

    def get_left(self):
        return self.__left

    def get_right(self):
        return self.__right

    def get_value(self):
        return self.__value


def all_paths_sums_to_n_helper(root, n, arr):
    val = root.get_value()
    arr.append(val)
    arr_sum = sum(arr)
    if arr_sum == n:
        yield tuple(arr)
        arr = []
    left, right = root.get_left(), root.get_right()
    if not arr:
        if left:
            yield from all_paths_sums_to_n_helper(left, n, [])
        if right:
            yield from all_paths_sums_to_n_helper(right, n, [])
    else:
        if left:
            set1 = set(all_paths_sums_to_n_helper(left, n, []))
            set2 = set(all_paths_sums_to_n_helper(left, n, arr[:]))
            for elm in set1.union(set2):
                yield elm

        if right:
            set3 = set(all_paths_sums_to_n_helper(right, n, []))
            set4 = set(all_paths_sums_to_n_helper(right, n, arr[:]))
            for elm in set3.union(set4):
                yield elm


def all_paths_sums_to_n(root, n):
    for tup in all_paths_sums_to_n_helper(root, n, []):
        yield list(tup)


# def all_paths_sums_to_n_helper(root, n, arr):
#     arr_sum = sum(arr)
#     if arr_sum == n:
#         yield arr
#         arr = []
#     if arr_sum > n:
#         arr = []
#     arr_sum = sum(arr) + root.get_value()
#     will_add = arr_sum == n
#     if will_add:
#         arr.append(root.get_value())
#         yield arr
#         arr = []
#     if not will_add:
#         if root.get_right():
#             yield from all_paths_sums_to_n_helper(root.get_right(), n, arr[:])
#         if root.get_left():
#             yield from all_paths_sums_to_n_helper(root.get_left(), n, arr[:])
#     arr.append(root.get_value())
#     if root.get_right():
#         yield from all_paths_sums_to_n_helper(root.get_right(), n, arr[:])
#     if root.get_left():
#         yield from all_paths_sums_to_n_helper(root.get_left(), n, arr[:])

node3 = TreeNode(8, TreeNode(3, TreeNode(1), TreeNode(6, TreeNode(4), TreeNode(
    7))), TreeNode(-5, right=TreeNode(14, TreeNode(-1, right=TreeNode(-4)))))

paths = sorted(list(all_paths_sums_to_n(node3, 4)))
print(paths)
