class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

        # curr1   tmp1


head1 = Node("1", Node("2", Node("3", Node("4"))))
head2 = Node("a", Node("b", Node("c", Node("d"))))
# curr2   tmp2

"1 -> a -> 2 -> b -> 3 -> c -> 4 -> d -> None"


def zipper(head1, head2):
    curr1 = head1
    curr2 = head2
    while curr1:
        tmp1 = curr1.next
        tmp2 = curr2.next
        curr1.next = curr2
        curr2.next = tmp1
        curr1 = tmp1
        curr2 = tmp2


zipper(head1, head2)
curr1 = head1
while curr1:
    print(curr1.data)
    curr1 = curr1.next

print(curr1.data)
