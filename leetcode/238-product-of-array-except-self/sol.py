from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l_prod = 1
        r_prod = 1
        ans = [1] * n

        for l, r in zip(range(1, n), range(n - 2, -1, -1)):
            l_prod *= nums[l - 1]
            r_prod *= nums[r + 1]
            ans[l] *= l_prod
            ans[r] *= r_prod

        return ans
    
sol = Solution()
print(sol.productExceptSelf([-1, 1, 3, 2, -4, 1]))