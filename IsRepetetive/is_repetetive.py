from calendar import c


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.__head = Node("a", Node("b", Node("a", Node("b", Node("a")))))
        self.__tail = None

    def is_repetetive(self, lst):
        if not lst:
            return True
        arr_len = len(lst)
        curr_node_idx = 0
        curr_node = self.__head
        while curr_node:
            if lst[curr_node_idx % arr_len] != curr_node.data:
                return False
            curr_node_idx += 1
            curr_node = curr_node.next
        if (curr_node_idx+1 % arr_len) != 0:
            return False
        return True


ls = LinkedList()
print(ls.is_repetetive(["a", "b"]))
print(ls.is_repetetive(["a", "b", "a"]))
print(ls.is_repetetive(["a", "b", "a", "b"]))
print(ls.is_repetetive(["c"]))
