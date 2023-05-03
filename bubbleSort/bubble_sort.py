

def bubble_sort_helper(lst, idx, end):
    if end == idx:
        return
    curr_item = lst[idx]
    for i in range(idx+1, end):
        iterated_item = lst[i]
        if curr_item > iterated_item:
            lst[i] = curr_item
            lst[i-1] = iterated_item
        else:
            bubble_sort_helper(lst, i, end)
    bubble_sort_helper(lst, idx, end-1)


def bubble_sort(lst):
    bubble_sort_helper(lst, 0, len(lst))


lst = [4, 2, 3, 2, 5]
bubble_sort(lst)
