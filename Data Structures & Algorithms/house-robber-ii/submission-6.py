class Solution:
    def rob(self, nums: List[int]) -> int: 
        if len(nums) == 1:
            return nums[0]       
        n = len(nums)
        dp1 = [-1] * (n)
        dp2 = [-1] * (n)

        def f(i, end, dp):
            if i < end:
                return 0
            elif dp[i] != -1:
                return dp[i]
            else:
                rob = nums[i] + f(i - 2, end, dp)
                skip = f(i - 1, end, dp)

                dp[i] = max(rob, skip)
                return dp[i]
        

        return max(f(n - 1, 1, dp1), f(n - 2, 0, dp2))
        
# class Solution:
#     def rob(self, nums: List[int]) -> int:        
#         n = len(nums)
#         dp = [-1] * (n)

#         def f(i, arr):
#             if i < 0:
#                 return 0
#             elif dp[i] != -1:
#                 return dp[i]
#             else:
#                 rob = arr[i] + f(i - 2, arr)
#                 skip = f(i - 1, arr)

#                 dp[i] = max(rob, skip)
#                 return dp[i]
        

#         return max(f(n - 1, nums[:n - 1]), f(n - 1, nums[1:]))
        