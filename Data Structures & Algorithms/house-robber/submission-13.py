class Solution:
    def rob(self, nums: List[int]) -> int:
        
        cache = {}
        def f(i):
            if i < 0:
                return 0
            if i in cache:
                return cache[i]
            else:
                take = nums[i] + f(i - 2)
                nottake = f(i - 1)
                cache[i] = max(take, nottake)
                return cache[i]
        
        return f(len(nums) - 1)