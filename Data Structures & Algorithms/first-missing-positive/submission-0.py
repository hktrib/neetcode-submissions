class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        maxMissing = n + 1

        for i in range(n):
            # Keep swapping nums[i] to its correct position if:
            # 1. It is a positive integer within the range [1, n]
            # 2. It is not already at its correct destination index (nums[i] - 1)
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Correct destination index for nums[i] is nums[i] - 1
                correct_idx = nums[i] - 1
                # Swap nums[i] and nums[correct_idx]
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]

            
        # Second pass: find the first index that doesn't match its expected value
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1