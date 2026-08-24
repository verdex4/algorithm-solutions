def insertion_sort(arr: list[int]):
    n = len(arr)

    for i in range(1, n):
        pos = i
        key = arr[i]
        
        while pos > 0 and arr[pos - 1] > key:
            arr[pos] = arr[pos - 1]
            pos -= 1

        arr[pos] = key

    return arr