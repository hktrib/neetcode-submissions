class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = [-1] * n

        def f(i) -> int:
            if i >= n:
                return 0
            elif dp[i] != -1:
                return dp[i]
            else:
                rob = nums[i] + f(i + 2)
                skip = f(i + 1)
                dp[i] = max(rob, skip)

                return dp[i]

        return f(0)