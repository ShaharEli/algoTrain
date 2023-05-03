

[1, 2, 3, 4]
[]
[1]
[1, 2]
[1, 2, 3]


def subsets_helper(lst, sublist, start, ar):
    if len(lst) == start:
        ar.append(sublist[:])
        print(sublist[:])
        return

    subsets_helper(lst, sublist, start+1, ar)
    sublist.append(lst[start])
    subsets_helper(lst, sublist,  start+1, ar)
    sublist.pop()


xw


def get_prev(_):
    prevs = [None]

    def prev(new_val):
        prev_data = prevs[-1]
        prevs.append(new_val)
        return prev_data
    return prev


@get_prev
def last_in():
    pass


def all_subsets(lst):
    ar = []
    subsets_helper(lst, [], 0, ar)
    return ar


all_subsets = all_subsets([1, 2, 3])
print(all_subsets)
