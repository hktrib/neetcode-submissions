from collections import defaultdict

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost) - 1

        memo = defaultdict(lambda: -1)

        def f(i):
            if i < 0:
                return 0
            elif memo[i] != -1:
                return memo[i]
            else:
                left = cost[i] + f(i - 1)
                right = cost[i] + f(i - 2)
                memo[i] = min(left, right)
                return memo[i]
        
        return min(f(N - 1), f(N))