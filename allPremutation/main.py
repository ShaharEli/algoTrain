

def all_premutation(arr):
    return all_premutation_helper(arr, 0)


def all_premutation_helper(arr, idx):
    if idx >= len(arr)-1:
        print(arr)
        return arr
    all_premutation_helper(arr, idx+1)
    for i in range(idx+1, len(arr)):
        arr[idx], arr[i] = arr[i], arr[idx]
        all_premutation_helper(arr, idx+1)
        arr[idx], arr[i] = arr[i], arr[idx]


print(
    all_premutation([1, 2, 3])
)
