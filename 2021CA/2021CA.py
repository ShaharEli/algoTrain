

def is_magic_square(square):
    first_diagonal_sum = sum([square[i][i] for i in range(len(square))])
    second_diagonal_sum = sum([square[i][len(square) - i-1]
                              for i in range(len(square))])
    if first_diagonal_sum != second_diagonal_sum:
        return False
    for row in square:
        if sum(row) != first_diagonal_sum:
            return False
    for i in range(len(square)):
        if sum([square[j][i] for j in range(len(square))]) != first_diagonal_sum:
            return False

    return True


# square_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# square_2 = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
# print(
#     is_magic_square(square_1)

# )
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def closest_value_helper(root, target, prev):
    left, right, data = root.left, root.right, root.value
    if data == target:
        return data
    if abs(data - target) < abs(prev - target):
        next_val = data
    else:
        next_val = prev
    if target > data:
        if not right:
            return next_val
        else:
            return closest_value_helper(right, target, next_val)
    else:
        if not left:
            return next_val
        else:
            return closest_value_helper(left, target, next_val)


def closest_value(root, target):
    return closest_value_helper(root, target, root.value)


root = TreeNode(9)
root.left = TreeNode(5)
root.right = TreeNode(26)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)
root.right.right = TreeNode(30)
root.right.right.right = TreeNode(100)
# print(closest_value(root, 1))
# print(closest_value(root, 2))
# print(closest_value(root, 8))
# print(closest_value(root, 29))
# print(closest_value(root, 80))
# print(closest_value(root, 105))


def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    s1 = list(s1)
    s2 = list(s2)

    return not s1 and not s2


def tree_iter_helper(lst, bound):
    if not bound:
        yield ""
    elif bound == 1:
        yield from (lett for lett in lst)
    else:
        for lett in lst:
            for prev in tree_iter_helper(lst, bound-1):
                yield lett + prev


def lexico_iter(lst):
    i = 0
    while True:
        yield from tree_iter_helper(lst, i)
        i += 1


hi = lexico_iter(["a", "b", "c"])


def count_string_helper(n, prev):
    if n == 0:
        return 1
    if prev:
        return count_string_helper(n-1, 0)
    else:
        return count_string_helper(n-1, 0) + count_string_helper(n-1, 1)


def count_strings(n):
    if not n:
        return 1
    return count_string_helper(n, None)


print(count_strings(0))
# good strings are: “”
print(count_strings(1))
# good strings are: “0”, “1”
print(
    count_strings(2)

)
# # good strings are: “00”, “01”, “10”
print(count_strings(3))
print(count_strings(4))
print(count_strings(5))
# print(count_strings(6))


class Baker:
    shelf = []
    storage = dict()

    def __init__(self, product, ingredients):
        self.product = product
        self.ingredients = ingredients
        self.ingredients_dict = dict()
        for elm in self.ingredients:
            self.ingredients_dict[elm] = self.ingredients_dict.get(elm, 0)+1

    def purchase(self, parts):
        for part in parts:
            Baker.storage[part] = Baker.storage.get(part, 0)+1

    def __str__(self):
        string = f"Bakes {self.product} - "

        string += ", ".join([f"{v} {k}" for k,
                            v in self.ingredients_dict.items()])
        return string

    def bake(self):
        for k, v in self.ingredients_dict.items():
            if Baker.storage.get(k, -1) < v:
                raise Exception(
                    f"Not enough ingredients in storage for {self.product}")
        for k, v in self.ingredients_dict.items():
            Baker.storage[k] -= v
        Baker.shelf.append(self.product)
        return True


dd = Baker("nuts_delight", ["sucar", "glour", "glour", "hemaa"])

dan = Baker("nuts_delight", ["nuts", "maple", "sugar", "cider", "almonds",
                             "nuts"])
dan.purchase(["maple", "sugar", "nuts", "maple", "cider"])
dan.purchase(["nuts", "almonds"])
gal = Baker("healthy_bounty", ["maple", "tahini", "coconut", "coconut oil",
                               "dark chocolate"])
dan.purchase(["tahini", "tahini", "coconut", "coconut oil", "dark chocolate"])
dan.bake()
# print(
#     Baker.shelf

# )

# gal.bake()
# print(
#     Baker.shelf

# )
# print(dan)
