if lst[mid-1] < lst[mid]:
        return find_discontinuity_helper(lst, start, mid)
    if lst[mid] < lst[mid+1]:
        return find_discontinuity_helper(lst, mid, end)