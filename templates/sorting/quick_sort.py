def quick_sort_simple(arr: list[int]):
    """Simple and stable version, but O(nlog(n)) space complexity"""
    n = len(arr)
    if n <= 1:
        return arr
    
    mid = n // 2
    pivot = arr[mid]
    left, middle, right = [], [], []

    for i in range(n):
        if arr[i] < pivot:
            left.append(arr[i])
        elif arr[i] == pivot:
            middle.append(arr[i])
        else:
            right.append(arr[i])

    left = quick_sort_simple(left)
    right = quick_sort_simple(right)

    return left + middle + right

def quick_sort_lomuto(arr: list[int], low: int = 0, high: int | None = None):
    """Classic Lomuto Scheme in-place, O(log(n)) space complexity"""
    def partition(arr: list[int], low: int, high: int):
        pivot = arr[high]
        i = low # next pos for insertion x < pivot
        for j in range(low, high):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[high] = arr[high], arr[i]
        return i

    if high is None:
        high = len(arr) - 1

    if high <= low:
        return

    pivot_pos = partition(arr, low, high)
    quick_sort_lomuto(arr, low, pivot_pos - 1)
    quick_sort_lomuto(arr, pivot_pos + 1, high)

    return arr


print(quick_sort_simple([7, 2, 5, 1, 6, 8, 5, 3, 4]))
print(quick_sort_lomuto([7, 2, 5, 1, 6, 8, 5, 3, 4]))