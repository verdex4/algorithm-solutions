from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set() # elements we already seen
        for x in nums:
            if x in seen: # O(1)
                return True
            seen.add(x)
        return False
    
sol = Solution()

print(sol.containsDuplicate([1, 2, 3, 5, 4]))
print(sol.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))