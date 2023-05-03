

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


all_increasing(arr)
