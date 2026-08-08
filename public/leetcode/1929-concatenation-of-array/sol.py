from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums

sol = Solution()
print(sol.getConcatenation([1, 3, 2, 1]))