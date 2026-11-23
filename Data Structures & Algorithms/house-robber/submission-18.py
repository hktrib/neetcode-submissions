class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        dp = {}

        def f(i):
            if i < 0:
                return 0
            elif i in dp:
                return dp[i]
            else:
                dp[i] = max(nums[i] + f(i - 2), f(i - 1))
                return dp[i]

        return f(N - 1)