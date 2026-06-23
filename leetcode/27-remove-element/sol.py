class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for n in nums:
            if n != val:
                k += 1
        
        free_pos = k
        for i in range(k):
            if nums[i] == val:
                while nums[free_pos] == val:
                    free_pos += 1
                nums[i], nums[free_pos] = nums[free_pos], nums[i]
                #print(f"added {i} -> {free_pos}")
                free_pos += 1
                
        print(nums)
        return k

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k], nums[i] = nums[i], nums[k]
                k += 1
            
        print(nums)
        return k
            
    
sol = Solution()
print(sol.removeElement([0,1,2,2,3,0,2,4], 2))