

def merge_sort(lst):
    if len(lst) == 1:
        return lst[0]
    mid = len(lst) // 2
    right = lst[:mid]
    left = lst[mid:len(lst)]
    merge_sort(right)
    merge_sort(left)
