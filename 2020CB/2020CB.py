

def check_if_valid(intval, curr):
    if not curr:
        return True
    if intval in curr:
        return False
    min_val = max(curr, key=lambda x: x[0])[0]
    max_val = min(curr, key=lambda x: x[1])[1]
    x, y = intval
    if x >= max_val:
        return False
    if y <= min_val:
        return False
    return True


def inter_helper(intvals, curr, arr):
    for intaval in intvals:
        if check_if_valid(intaval, curr):
            curr.append(intaval)
            inter_helper(intvals, curr, arr)
            curr.pop()
    arr.append(len(curr))


def inter(intvals):
    arr = []
    inter_helper(intvals, [], arr)
    return max(arr)


# intvals = [(3, 6), (2, 5), (2, 3)]
# print(
    # inter(intvals)
# )


def down_mult(seed, up_bound):
    start = up_bound - (up_bound % seed)
    if start == seed:
        return
    yield from range(start, seed, -seed)
    yield seed


def tree(data, subtrs=[]): return [data] + list(subtrs)
def data(t): return t[0]
def subtrs(t): return t[1:]
def leaf(t): return not subtrs(t)


def bound_track_max_helper(tr, bound, curr, arr):
    if 0 < len(curr) <= bound:
        arr.append(
            
        )
    if len(curr) > bound:
        return
    if not tr:
        return
    curr_data = data(tr)
    subs = subtrs(tr)
    if not subs:
        curr.append(curr_data)
        if 0 < len(curr) <= bound:
            arr.append(
                
            )
        curr.pop()
    else:
        bound_track_max_helper(subs[0], bound, [], arr)
        curr.append(curr_data)
        bound_track_max_helper(subs[0], bound, curr, arr)
        curr.pop()
        if len(subs) == 2:
            bound_track_max_helper(subs[1], bound, [], arr)
            curr.append(curr_data)
            bound_track_max_helper(subs[1], bound, curr, arr)
            curr.pop()


def bound_track_max(tr, bound):
    arr = []
    bound_track_max_helper(tr, bound, [], arr)
    if not arr:
        return []
    return sorted(arr, key=sum, reverse=True)[0]


tr1 = tree(4, [tree(3, [tree(8), tree(2)]),
           tree(7, [tree(5, [tree(6), tree(1)])])])
tr2 = tree(2, [tree(3, [tree(5), tree(6)]), tree(7)])
tr3 = tree(2, [tree(3, [tree(5), tree(6, [tr1])]), tree(7)])

# print(bound_track_max(tr1, 1))  # [8]
# print(bound_track_max(tr1, 2))  # [7, 5]
# print(bound_track_max(tr1, 3))  # [7, 5, 6
# print(bound_track_max(tr1, 4))  # [4, 7, 5, 6]
# print(bound_track_max(tr1, 5))
# [4, 7, 5, 6]


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head


def add_to_sorted(L1, L2):
    if not L1 and not L2:
        return None
    if not L2:
        return L1
    l2_nodes = []
    curr = L2.head
    while curr:
        l2_nodes.append((curr, curr.data))
        curr = curr.next
    l2_nodes = sorted(l2_nodes, key=lambda x: x[1])
    curr = L1.head
    if not curr:
        L1.head = l2_nodes[0][0]
        l2_nodes.pop(0)
        curr = L1.head
        for node in l2_nodes:
            curr.next = node[0]
            curr = curr.next
        curr.next = None

    while curr:
        next = curr.next
        if not next:
            if not l2_nodes:
                break
            for node in l2_nodes:
                curr.next = node[0]
                curr = curr.next
            curr.next = None
            break

        curr_data = curr.data
        while True:
            if curr_data <= l2_nodes[0][1] <= next.data:
                curr.next = l2_nodes[0][0]
                curr.next.next = next
                l2_nodes.pop(0)
            else:
                break
        curr = curr.next

    return L1


# hi = Node(1, Node(3, Node(7, Node(12))))
# bi = Node(15, Node(6, Node(2)))

# ko = add_to_sorted(LinkedList(None), LinkedList(Node(9, Node(1))))
# hed = ko.head
# while hed:
#     print(hed.data)
#     hed = hed.next
