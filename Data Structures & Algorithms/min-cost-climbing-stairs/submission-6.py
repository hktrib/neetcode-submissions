class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 1:
            return cost[0]

        dp = [float('inf')] * n

        def f(i):
            if i >= n:
                return 0
            elif dp[i] != float('inf'):
                return int(dp[i])
            else:
                left = f(i + 1) + cost[i]
                right = f(i + 2) + cost[i]

                dp[i] = min(left, right)

                return int(dp[i])

        
        return min(f(0), f(1))