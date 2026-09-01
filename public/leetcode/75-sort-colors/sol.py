class Solution:
    def sortColorsCountingSort(self, nums: list[int]) -> None:
        count = [0] * 3
        for num in nums:
            count[num] += 1

        color = 0
        i = 0
        while color < 3:
            while count[color]:
                nums[i] = color
                count[color] -= 1
                i += 1
            color += 1

    def sortColorsTwoPointers(self, nums: list[int]) -> None:
        i, j = 0, len(nums) - 1
        k = 0
        while k <= j:
            if nums[k] == 0:
                nums[i], nums[k] = nums[k], nums[i]
                i += 1
            elif nums[k] == 2:
                nums[j], nums[k] = nums[k], nums[j]
                j -= 1
                k -= 1

            k += 1

        return

sol = Solution()
nums = [0, 1, 0, 2, 2, 2, 1, 0, 1, 2, 0]
sol.sortColorsTwoPointers(nums)
print(nums)
