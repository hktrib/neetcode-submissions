class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        # Helper function where dp is local to each run
        def helper(start, end):
            # dp array only needs to cover the active range, or size n
            dp = [-1] * len(nums)
            
            def f(i):
                if i < start:
                    return 0
                if dp[i] != -1:
                    return dp[i]
                
                rob_curr = nums[i] + f(i - 2)
                skip_curr = f(i - 1)
                
                dp[i] = max(rob_curr, skip_curr)
                return dp[i]
                
            return f(end)

        # Case 1: Exclude first house (indices 1 to n-1)
        # Case 2: Exclude last house (indices 0 to n-2)
        return max(helper(1, n - 1), helper(0, n - 2))