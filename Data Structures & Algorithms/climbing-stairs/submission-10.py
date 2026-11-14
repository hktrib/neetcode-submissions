class Solution:
    def climbStairs(self, n: int) -> int:
        
        numOfWays = 0
        dpArray = [-1] * (n + 1) 
        
        def f(stepIndex: int) -> None:
            nonlocal numOfWays
            if stepIndex < 0:
                return 0
            elif stepIndex == 0:
                return 1
            elif dpArray[stepIndex] != -1:
                return dpArray[stepIndex]
            else:
                dpArray[stepIndex] = f(stepIndex - 1) + f(stepIndex - 2)
                return dpArray[stepIndex]
        
        return f(n)
        # return numOfWays


