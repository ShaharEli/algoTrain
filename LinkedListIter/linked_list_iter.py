from re import T


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def get_reverse_iter(head):
    data_list = []
    curr = head
    while curr.next:
        data_list.insert(0, curr.data)
        curr = curr.next
    yield curr.data
    for x in data_list:
        yield x


lst = Node("a", Node("b", Node("c", Node("d", Node("e", Node("f"))))))

for x in get_reverse_iter(lst):
    print(x)
