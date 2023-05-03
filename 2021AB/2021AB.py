
# class Node:
#     def __init__(self, data, left=None, right=None):
#         self.data = data
#         self.left = left
#         self.right = right


# def find_path_helper(root, k, curr):
#     if not root:
#         return None
#     left, right, data = root.left, root.right, root.data
#     if not right and not left:
#         if k-data == 0:
#             return curr+[data]
#         return None
#     if left:
#         left_checker = find_path_helper(left, k-data, curr+[data])
#         if left_checker:
#             return left_checker
#     if right:
#         right_checker = find_path_helper(right, k-data, curr+[data])
#         if right_checker:
#             return right_checker


# def find_path(root, k):
#     return find_path_helper(root, k, [])


# root = Node(1, Node(2, Node(8), Node(0, Node(9))),
#             Node(-7, Node(5, Node(0), Node(9)), Node(4, None, Node(-3))))
# # print(find_path(root, 8))


# def doohickey(x): return lambda *y, **k: 6


# @doohickey
# def func1(a, b, c=None):
#     if a > b:
#         return c


# @doohickey
# def func2(g, e):
#     return str(g+e)+"hello!"


# print(func1(3, 4, c="joe!"), func2(e=7, g=8))

# def even_odd(lst):
#     return sorted(lst, key=lambda x: x % 2)


# print(even_odd([5, 4, -6, 9, 7]))
# source = [1, 2]
# source[1] = source


# def check_ids(elm, sett):
#     if not isinstance(elm, list):
#         return
#     if id(elm) in sett:
#         return
#     sett.add(id(elm))
#     for elms in elm:
#         check_ids(elms, sett)


# ids = set()
# ids2 = set()

# print(source)
# x = [[source[:] for i in range(10)] for j in range(10)]
# check_ids(x, ids)
# print(len(ids))
# y = [i[:] for i in x]
# check_ids(y, ids2)
# print(len(ids2.difference(ids)))
# print(len(ids))

# def rotate(s, d):
#     x = s[:len(s)-d]
#     y = s[len(s)-d:]
#     return (y+x)


# print("abcde")
# print(rotate("abcde", 1))

import string


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def find_path_helper(root, k, path):
    if not root:
        if not k:
            return path
        return None
    left, right, data = root.left, root.right, root.data
    left_checker = find_path_helper(left, k-data, path+[data])
    if left_checker:
        return left_checker
    right_checker = find_path_helper(right, k-data, path+[data])
    return right_checker


def find_path(root, k):
    return find_path_helper(root, k, [])


# root = Node(1, Node(2, Node(8), Node(0, Node(9))),
#             Node(-7, Node(5, Node(0), Node(9)), Node(4, None, Node(-3))))
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.vac_num = 0
        self.spouse = None

    def get_vac_num(self):
        return self.vac_num

    def set_vac_num(self, n):
        self.vac_num = n

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def marry(self, spouse):
        if not spouse:
            raise Exception
        if spouse.get_spouse() and spouse.get_spouse() != self.spouse:
            raise Exception
        spouse.spouse = self
        self.spouse = spouse

    def get_spouse(self):
        return self.spouse


# class VaccinationCenter:x
# lst1 = [(5, 2), 0, "-7", 4, 8]
# lst2 = [1, 2, 3, 4, 5]

# try:
#     for item in lst1:
#         try:
#             print(lst2[item] // item, end=' ')
#         except(TypeError):
#             print("a", end=' ')
#         except(ZeroDivisionError):
#             print("b", end=' ')
#         except(IndexError):
#             print("c", end=' ')
# except:
#     print("e", end=' ')
# finally:
#     print("f", end=' ')

# def t(n):
#     if n <= 0:
#         return 0
#     else:
#         return 1+t((n-1)//2)


# print([t(i) for i in range(18)])

x = [[3, 2], [4, 5], [8, 1], [9, 3]]
y = [item for item in "".join(["".join([str(i[0]), str(i[1])]) for i in x])]
# print([[a, b, c, d] for a, b, c, d in [y[3:7]]])


def find_ingredient(recipes, item):
    for recipe in recipes:
        if item in recipe[1]:
            return recipe[0]

    return None


def get_ingredients_helper(final_item, recipes, curr):
    next_ingridents = find_ingredient(recipes, final_item)
    if not next_ingridents:
        return curr
    curr.remove(final_item)
    for ingredient in next_ingridents:
        curr.add(ingredient)
        get_ingredients_helper(ingredient, recipes, curr)
    return curr


def get_ingredients(final_item, recipes):
    return get_ingredients_helper(final_item, recipes, {final_item})


recipes = [
    (("water", "flour", "salt"), ("dough", "messy counter")),
    (("frozen dough", "water",), ("dough")),
    (("dough", "garlic"), ("garlic bread", "dirty oven")),
    (("garlic bread", "cheese"), ("sandwich")),
    (("envelope", "paper", "stamp"), ("letter"))
]
# print(get_ingredients("sandwich", recipes))


def find_max_prefix_sum_helper(lst, i, summ, best, maxx):
    if i == len(lst):
        return best
    elm = lst[i]
    summ += elm
    if summ > maxx:
        maxx = summ
        best = i
    return find_max_prefix_sum_helper(lst, i+1, summ, best, maxx)


# print(
#     find_max_prefix_sum([1, -5, 9, -12, 3, 3, 3, 2])
# )

# print(
#     find_max_prefix_sum([1, -5, 9, 7])
# )

def find_max_prefix_sum(lst):
    return find_max_prefix_sum_helper(lst, 0, 0, 0, 0)+1


LETTERCONVERSION = ord('a')


def letter_to_index(let):
    return ord(let) - LETTERCONVERSION


def index_to_letter(num):
    return chr(ord('a') + num)


def create_vigenere_square():
    square = list()
    alphabet_list = list(string.ascii_lowercase)
    for i in range(len(alphabet_list)):
        square.append(alphabet_list[i:] + alphabet_list[:i])
    return square


vs = create_vigenere_square()


def encrypt(msg, key):
    return "".join([vs[letter_to_index(key[i % len(key)])][letter_to_index(msg[i])] for i in range(len(msg))])


def decrypt(msg, key):
    stri = ""
    for i, elm in enumerate(msg):
        decrypt_line = vs[letter_to_index(key[i % len(key)])]
        stri += index_to_letter(decrypt_line.index(elm))
    return stri
    # return "".join([vs[index_to_letter(key[i % len(key)])][index_to_letter(msg[i])] for i in range(len(msg))])


print(decrypt("dirm", "beg"))
