

import random


def get_pivot(arr):
    return random.randint(0, len(arr)-1)


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = get_pivot(arr)
    pivot_val = arr[pivot]
    greater = []
    smaller = []
    for idx, val in enumerate(arr):
        if idx == pivot:
            continue
        if val >= pivot_val:
            greater.append(val)
        else:
            smaller.append(val)
    return quicksort(smaller) + [pivot_val]+quicksort(greater)


print(
    quicksort([10, 2, 3, 4, 5, 6, 7, 8, 9])

)
