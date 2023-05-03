
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
a.next = b
b.next = c
c.next = d
d.next = a


head = a
while head:
    print(head.data, end=" ")
    if head.next == a:
        print(head.next.data)
        break
    head = head.next


def reverse_circled_linked_list(head):
    curr = head
    prev = None
    started = True
    while (curr != head or started):
        started = False
        next = curr.next
        next_next = next.next
        next.next = curr
        if prev:
            curr.next = prev
        prev = next
        curr = next_next
    curr.next = prev


reverse_circled_linked_list(a)
head = a
while True:
    print(head.data, end=" ")
    if head.next == a:
        print(head.next.data)
        break
    head = head.next
