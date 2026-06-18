class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # tabulation
        
        # memo = [-1 for i in range(amount + 1)]
        # def f(remainder):
        #     nonlocal memo
        #     if remainder == 0:
        #         return 0
        #     elif memo[remainder] != -1:
        #         return memo[remainder]
        #     else:
        #         minVal = float('inf')
        #         for i in range(len(coins)):
        #             if remainder >= coins[i]:
        #                 res = f(remainder - coins[i])
        #                 if res != -1:
        #                     minVal = min(minVal, 1 + res)
                
        #         memo[remainder] = -1 if minVal == float('inf') else minVal

        #         return memo[remainder]
        

        dp = [-1 for i in range(amount + 1)]
        dp[0] = 0


        for remainder in range(1, amount + 1):
            minVal = float('inf')
            for j in range(len(coins)):
                if remainder >= coins[j]:
                    res = dp[remainder - coins[j]]
                    if res != -1:
                        minVal = min(minVal, 1 + res)
            
            dp[remainder] = -1 if minVal == float('inf') else minVal

        return dp[amount]