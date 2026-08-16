class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = [-1] * (n)
        
        def f(i):
            if i == n:
                return 1
            elif i > n:
                return 0
            elif dp[i] != -1:
                return dp[i]
            else:
                left = f(i + 1)
                right = f(i + 2)

                dp[i] = left + right
                return dp[i]

        return f(0)
