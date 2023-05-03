

def find_discontinuity(lst):
    return find_discontinuity_helper(lst, 0, len(lst)-1)


def find_discontinuity_helper(lst, start, end):
    if not lst:
        return
    mid = (end - start)//2
    if lst[mid+1] < lst[mid] and lst[mid] > lst[mid-1]:
        return mid
    if lst[mid-1] < lst[mid]:
        return find_discontinuity_helper(lst, start, mid)
    if lst[mid] < lst[mid+1]:
        return find_discontinuity_helper(lst, mid, end)


# lst = [10, 11, 12, 1, 2, 3]

# print(find_discontinuity(lst))


# def all_increasing_helper(arr, lst, idx):
#     if idx == len(arr):
#         print(lst, end=" ")
#         return
#     all_increasing_helper(arr, lst, idx+1)
#     lst.append(arr[idx])
#     all_increasing_helper(arr, lst, idx+1)
#     lst.pop()
def all_increasing_helper(arr, lst, idx):
    if idx == len(arr):
        print(lst, end=" ")
        return
    all_increasing_helper(arr, lst, idx+1)
    lst.append(arr[idx])
    all_increasing_helper(arr, lst, idx+1)
    lst.pop()


def all_increasing(arr):
    all_increasing_helper(sorted(arr), [], 0)


arr = [1, 4, 3, 2]


def find_allPrem_helper(arr, lst, idx):
    if idx == len(arr):
        print(lst)
        return
    find_allPrem_helper(arr, lst, idx+1)
    lst.append(arr[idx])
    find_allPrem_helper(arr, lst, idx+1)
    lst.pop()


def find_allPrem(lst):
    find_allPrem_helper(lst, [], 0)


n = 1000


def deepen(lst, n):
    return [lst[:] for i in range(n)]


lst1 = list(range(n))
print(len(set([id(lst) for lst in lst1])))
lst1.append(lst1)
lst2 = deepen(lst1, n)
lst3 = deepen(lst2, n)


class SomeIter:

    def __init__(self, max):
        self._cur = 0
        self._max = max

    def __iter__(self):
        return self

    def __next__(self):
        self._cur += 1
        if self._cur >= self._max:
            raise StopIteration()
        return self._cur


hi = SomeIter(2)
