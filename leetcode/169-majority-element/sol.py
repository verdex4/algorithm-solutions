class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        cand = None
        cnt = 0
        for num in nums:
            if cnt == 0:
                cand = num
                cnt = 1
            elif num == cand:
                cnt += 1
            else:
                cnt -= 1
        
        return cand

sol = Solution()
print(sol.majorityElement([2,2,1,1,1,2,2]))