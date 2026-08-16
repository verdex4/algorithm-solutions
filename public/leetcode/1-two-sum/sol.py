class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for j in range(len(nums)):
            needed = target - nums[j]
            if needed in seen:
                return [seen[needed], j]
            seen[nums[j]] = j

        return []

sol = Solution()
print(sol.twoSum([1, 1, 1, 3, 6, 2, 3, 55, 4], 7))