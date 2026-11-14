class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()

        # since only one pair of indices i and j satisfy the 
        # condition we can assume there are no duplicate numbers
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            else:
                seen[num] = i

        
        return []
            