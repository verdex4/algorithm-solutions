def counting_sort(arr: list[int], exp: int):
    count = [0] * 10
    for i in range(len(arr)):
        digit = (arr[i] // exp) % 10
        count[digit] += 1

    last_pos = [count[0] - 1]
    for i in range(1, len(count)):
        p = last_pos[i - 1] + count[i]
        last_pos.append(p)

    res = [0] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        res[last_pos[digit]] = arr[i]
        last_pos[digit] -= 1

    arr[:] = res

def radix_sort(arr: list[int]):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:   
        counting_sort(arr, exp)
        exp *= 10

def solve(arr: list[int]):
    if not arr:
        return []
    
    negatives = [-num for num in arr if num < 0]
    positives = [num for num in arr if num >= 0]

    if negatives:
        radix_sort(negatives)
        negatives = [-num for num in reversed(negatives)]
    if positives:
        radix_sort(positives)

    return negatives + positives

print(solve([5, -2, 3, 1, 3, 2, 1, 7, -10]))