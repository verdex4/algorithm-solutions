from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_freq = 0
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            max_freq = max(max_freq, freq[num])
        freq_groups = [[] for _ in range(max_freq + 1)]
        for num, f in freq.items():
            freq_groups[f].append(num)
        res = []
        for i in range(len(freq_groups) - 1, -1, -1):
            for num in freq_groups[i]:
                res.append(num)
                if len(res) == k:
                    return res

sol = Solution()
print(sol.topKFrequent([1,1,1,2,2,3], k = 2))
print(sol.topKFrequent([1,1,2,2,3,3,4,4,4,4], k = 3))
print(sol.topKFrequent([1,2,3,2,3,3,4,1,3,1,2,1], k = 3))
