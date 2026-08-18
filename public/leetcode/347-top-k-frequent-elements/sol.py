from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        cntr = Counter(nums)
        max_freq = max(cntr.values())
        buckets = [[] for _ in range(max_freq + 1)]

        for num, f in cntr.items():
            buckets[f].append(num)

        res = []
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res

        # if k > n return sorted n elements
        return res

sol = Solution()
print(sol.topKFrequent([1,1,1,2,2,3], k = 2))
print(sol.topKFrequent([1,1,2,2,3,3,4,4,4,4], k = 3))
print(sol.topKFrequent([1,2,3,2,3,3,4,1,3,1,2,1], k = 3))
