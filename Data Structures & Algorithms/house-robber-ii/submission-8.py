class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
            
        # Helper function for regular House Robber (Linear)
        def solve(arr):
            m = len(arr)
            dp = [-1] * m
            
            def f(i):
                if i == 0:
                    return arr[0]
                if i < 0:
                    return 0
                if dp[i] != -1:
                    return dp[i]
                
                rob_curr = arr[i] + f(i - 2)
                skip_curr = f(i - 1)
                
                dp[i] = max(rob_curr, skip_curr)
                return dp[i]
                
            return f(m - 1)

        # Case 1: Exclude the last house (nums[:-1])
        # Case 2: Exclude the first house (nums[1:])
        return max(solve(nums[:-1]), solve(nums[1:]))