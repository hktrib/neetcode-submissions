class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        
        dpFirst = {}
        dpSecond = {}
        def f(i, arr, dp):
            if i < 0:
                return 0
            elif i in dp:
                return dp[i]
            else:
                dp[i] = max(arr[i] + f(i - 2, arr, dp), f(i - 1, arr, dp))
                return dp[i]
        
        arr1, arr2 = nums[:-1], nums[1:]
        
        return max(f(len(arr1) - 1, arr1, dp=dpFirst), f(len(arr2) - 1, arr2, dp=dpSecond))