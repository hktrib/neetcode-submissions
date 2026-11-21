class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        N = len(nums)

        res = []

        for i in range(N):
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            target = nums[i]
            l, r = i + 1, N - 1

            while l < r:
                currSum = target + nums[l] + nums[r]

                if currSum < 0:
                    l += 1
                elif currSum > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < N and nums[l] == nums[l - 1]:
                        l += 1
            
        return res
