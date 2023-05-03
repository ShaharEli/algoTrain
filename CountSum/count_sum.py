
# def all_subset_helper(lst, subset, all_subsets_arr, idx):
#     if len(lst) == idx:
#         all_subsets_arr.append(subset[:])
#         return
#     all_subset_helper(lst, subset, all_subsets_arr, idx+1)
#     subset.append(lst[idx])
#     all_subset_helper(lst, subset, all_subsets_arr, idx+1)
#     subset.pop()


# def all_subsets(lst):
#     all_subsets_arr = []
#     all_subset_helper(lst, [], all_subsets_arr, 0)
#     return all_subsets_arr


# def count_sum(a, s):
#     all_subsets_arr = all_subsets(a)
#     count = 0
#     for x in all_subsets_arr:
#         if sum(x) == s:
#             count += 1
#     return count


def count_sum_helper(a, s, idx):
    if idx == len(a):
        if not s:
            return 1
        return 0
    return count_sum_helper(a, s-a[idx], idx+1) + count_sum_helper(a, s, idx+1)


def count_sum(a, s):
    return count_sum_helper(a, s, 0)


print(
    count_sum([1, 2, 3, 0], 3)

)
