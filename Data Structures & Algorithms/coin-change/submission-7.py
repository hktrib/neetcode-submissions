class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        

        dp = {}
        def f(rem):
            if rem == 0:
                return 0
            elif rem < 0:
                return float('inf')
            elif rem in dp:
                return dp[rem]
            else:
                minCoins = float('inf')
                for i in range(len(coins)):
                    minCoins = min(minCoins, 1 + f(rem - coins[i]))
                
                dp[rem] = minCoins

                return dp[rem]
        
        ans = f(amount)
        return ans if ans != float('inf') else -1