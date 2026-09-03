class Solution:
    def firstMissingPositiveCycleSort(self, nums: list[int]) -> int:
        n = len(nums)

        for i in range(n):
            j = nums[i] - 1
            while 1 <= nums[i] <= n and nums[i] != nums[j] and i != j:
                nums[i], nums[j] = nums[j], nums[i]
                j = nums[i] - 1

        for i in range(n):
            if nums[i] != i + 1:    
                return i + 1

        return n + 1

    def firstMissingPositiveSignMarking(self, nums: list[int]) -> int:
        n = len(nums)

        for i in range(n):
            if nums[i] < 0:
                nums[i] = 0

        for i in range(n):
            val = abs(nums[i])
            if 0 < val <= n:
                j = val - 1
                if nums[j] > 0:
                    nums[j] = -nums[j]
                elif nums[j] == 0:
                    nums[j] = -n - 1

        for i in range(n):
            if nums[i] >= 0:
                return i + 1

        return n + 1

sol = Solution()
print(sol.firstMissingPositiveSignMarking([1, 1]))