class Solution:
    def tribonacci(self, n: int) -> int:
        self.memo = {}
        
        def dfs(i):
            if i == 0:
                return 0
            elif i == 1:
                return 1
            elif i == 2:
                return 1
            elif i in self.memo:
                return self.memo[i]
            else:
                res = dfs(i - 1) + dfs(i - 2) + dfs(i - 3)
                self.memo[i] = res
                return self.memo[i]

        return dfs(n)