def counting_sort(arr: list[int]) -> list[int]:
    """For int array (any numbers including negatives)"""
    if not arr:
        return []
    
    min_val, max_val = min(arr), max(arr)
    count = [0] * (max_val - min_val + 1)

    for x in arr:
        count[x - min_val] += 1

    res = []
    for i in range(len(count)):
        if count[i]:
            num = i + min_val
            res.extend([num] * count[i])

    return res

print(counting_sort([1, 4, 6, -1, 3, 0, 2, -2, 4]))