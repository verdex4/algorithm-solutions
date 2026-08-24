def insertion_sort_base(arr: list[int]):
    n = len(arr)

    for i in range(1, n):
        pos = i
        key = arr[i]
        
        while pos > 0 and arr[pos - 1] > key:
            arr[pos] = arr[pos - 1]
            pos -= 1

        arr[pos] = key

    return arr

# NEETCODE INSERTION SORT CORE SKILLS

# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

class Solution:
    def insertionSort(self, pairs: list[Pair]) -> list[list[Pair]]:
        n = len(pairs)
        res = []

        for i in range(n):
            pos = i
            cur = pairs[i]

            while pos > 0 and pairs[pos - 1].key > cur.key:
                pairs[pos] = pairs[pos - 1]
                pos -= 1

            pairs[pos] = cur
            res.append(pairs.copy())

        return res

pairs = [Pair(3, "cat"), Pair(3, "bird"), Pair(2, "dog")]
res = Solution().insertionSort(pairs)
for it in res:
    print([f"({obj.key}, {obj.value})" for obj in it], sep=" ")