class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        l = 0
        r = len(nums) - 1

        last2point = len(nums) - 1
        while l < r:
            if nums[r] == 2:
                r -= 1
                last2point = r
            elif nums[l] != 2:
                l += 1
            else:
                nums[l], nums[r] = nums[r], nums[l]
                last2point = r
                r -= 1
                l += 1
        
        if r >= 0 and nums[r] == 2:
            r -= 1

        l = 0
        while l < r:
            if nums[r] == 1:
                r -= 1
            elif nums[l] != 1:
                l += 1
            else:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
                l += 1
        
        return None
