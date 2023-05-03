

def up_and_right_helper(n, k, lst, curr):
    if n == 0:
        lst.append("".join(curr + ["u" for _ in range(k)]))

        return
    if k == 0:
        lst.append("".join(curr + ["r" for _ in range(n)]))
        return
    curr.append("r")
    up_and_right_helper(n-1, k, lst, curr)
    curr.pop()
    curr.append("u")
    up_and_right_helper(n, k-1, lst, curr)
    curr.pop()


def up_and_right(n, k, lst):
    up_and_right_helper(n, k, lst, [])


lst = []
up_and_right(2, 1, lst)
print(lst)
