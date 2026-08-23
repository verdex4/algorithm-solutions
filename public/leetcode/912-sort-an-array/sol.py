class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        m = 5 * 10**4
        cnt = [0] * (m * 2 + 1)
        for num in nums:
            i = num + m
            cnt[i] += 1

        ans = []
        for i, count in enumerate(cnt):
            num = i - m
            if count:
                ans.extend([num] * count)

        return ans

sol = Solution()
print(sol.sortArray([5,1,1,2,0,0]))