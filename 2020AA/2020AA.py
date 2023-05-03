

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def equal_trees(x, y):
    if not x and not y:
        return True
    if [x, y].count(None) > 0:
        return False
    if x.value != y.value:
        return False
    x_left, x_right = x.left, x.right
    y_left, y_right = y.left, y.right
    if [x_left, x_right].count(None) != [y_left, y_right].count(None):
        return False
    return (equal_trees(x_left, y_left) and equal_trees(x_right, y_right)) or (equal_trees(x_left, y_right) and equal_trees(x_right,  y_left))


# hi = TreeNode(6, TreeNode(3, TreeNode(1), TreeNode(7)), TreeNode(
    # 8, TreeNode(4, TreeNode(9), TreeNode(1)), TreeNode(2, None, TreeNode(3))))
# bye = TreeNode(6, TreeNode(
    # 8, TreeNode(4, TreeNode(9), TreeNode(1)), TreeNode(2, None, TreeNode(3))), TreeNode(3, TreeNode(1), TreeNode(7)))
# print(equal_trees(hi, bye))


class MyMapIter:

    def __init__(self, func, *iters):
        self.func = func
        self.iters = iters

    def __iter__(self):
        return self

    def __next__(self):
        try:
            nexts = [next(iterr) for iterr in self.iters]
            return self.func(*nexts)
        except:
            raise StopIteration()


def find_closest(lst, elm):
    if len(lst) == 2:
        return (lst[0], lst[1])
    end = len(lst) - 2
    start = 1
    prev_start = lst[0]
    prev_end = lst[-1]
    dis = abs((prev_start+prev_end)-elm)
    couple = (prev_start, prev_end)

    while start <= end:
        curr_start = lst[start]
        curr_end = lst[end]
        curr_dis = [abs((curr_start+curr_end)-elm),
                    (curr_start, curr_end)]
        curr_from_prev_start = [
            abs((curr_start+prev_start)-elm), (curr_start, prev_start)]
        curr_from_prev_end = [
            abs((curr_start+prev_end)-elm), (curr_start, prev_end)]
        curr_from_prev_start_end = [
            abs((curr_end+prev_start)-elm), (curr_end, prev_start)]
        curr_from_prev_end_start = [
            abs((curr_end+prev_end)-elm), (curr_end, prev_end)]
        dis, couple = sorted([curr_dis, curr_from_prev_start, curr_from_prev_end,
                             curr_from_prev_start_end, curr_from_prev_end_start, [dis, couple]], key=lambda x: x[0])[0]

        prev_start = curr_start
        curr_end = curr_end
        start += 1
        end -= 1
    return couple


# print(
    # find_closest([10, 22, 28, 29, 30, 40], 54)
# )

def gen_str_helper(n, curr):
    if len(curr) == n:
        print(curr)
        return
    if not len(curr):
        gen_str_helper(n, "1")
        gen_str_helper(n, "0")
    else:
        gen_str_helper(n, curr + "0")
        if curr[-1] != "1":
            gen_str_helper(n, curr + "1")


def gen_str(n):
    gen_str_helper(n, "")


gen_str(3)
gen_str(5)
