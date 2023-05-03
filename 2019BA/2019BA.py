

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, head):
        self.head = head

    def swap(self, node1, node2, is_head=False):
        node2_next = node2.next
        node2.next = node1
        node1.next = node2_next
        if is_head:
            self.head = node2

    def __str__(self):
        curr = self.head
        string = ""
        while curr:
            string += f"{curr.data} -> "
            curr = curr.next

        return string[:-3]

    def sort(self):
        length = 0
        curr = self.head
        prev = None
        while curr:
            curr = curr.next
            length += 1
        while length-1:
            start = 0
            runner = self.head
            prev = None
            while start < length-1:
                if runner.data > runner.next.data:
                    tmp = runner.next
                    self.swap(runner, runner.next, start == 0)
                    if prev:
                        prev.next = tmp
                    prev = tmp
                else:
                    prev = runner
                    runner = runner.next
                start += 1
            length -= 1


# ls = LinkedList(Node(9, Node(-3, Node(4, Node(1, Node(8))))))
# print(ls)
# ls.sort()
# print(ls)


def same_char_helper(s, k):
    c = 0
    data = s[k]
    for i in range(k, len(s)):
        if data != s[i]:
            return c
        else:
            c += 1
    return c


def describe_str(st1):
    start = 0
    build = ""
    while start != len(st1):
        build += st1[start]
        c = same_char_helper(st1, start)
        start += c
        build += str(c)
    return build


# print(describe_str("abbcccdeaa"))
class Child:
    def __init__(self, name, mother=None, father=None):
        self.name = name
        self.mother = mother
        self.father = father


def family_tree_helper(child, target):
    if not child:
        return False
    child_name, child_mother, child_father = child.name, child.mother, child.father
    if child_name == target:
        return True
    return family_tree_helper(child_mother, target) or family_tree_helper(child_father, target)


def family_tree(a, b):
    return family_tree_helper(a, b.name) or family_tree_helper(b, a.name)


# x = Child('Ety')
# y = Child('Malka', x)
# z = Child('Iosi', y, x)
# u = Child('Ely', z)
# v = Child('Avi')

# print(family_tree(u, x))
# print(family_tree(x, x))
# print(family_tree(v, x))


def rev_list_rec(lst):
    if not len(lst):
        return []
    if len(lst) == 1:
        return lst
    return [lst[-1]] + rev_list_rec(lst[1:-1])+[lst[0]]


def rev_list_rec_non(lst):
    copy = lst[:]
    for i in range((len(lst)+1)//2):
        copy[i], copy[len(lst)-i-1] = copy[len(lst)-i-1], copy[i]
    return copy


# lst = ["a", "b", 3, 5, [1, 2]]
# print(

    # rev_list_rec_non(lst)
# )
def mat_gen():
    def g(mat):
        row_turn = True
        while mat:
            if row_turn:
                row = mat[0]
                del mat[0]
                yield row
            else:
                column = []
                for i in range(len(mat)):
                    column.append(mat[i][0])
                    del mat[i][0]
                yield column

            row_turn = not row_turn
    return g


mat = [[1, 2, 3, 4], [2, 8, 6, 4], [5, 1, 7, 9]]
# print(list(zip(*mat)))

# g = mat_gen()(mat)
# for x in g:
#     print(x)
# print(mat)
