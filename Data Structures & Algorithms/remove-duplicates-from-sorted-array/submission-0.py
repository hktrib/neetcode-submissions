class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        n = len(nums)

        i = 0
        while i < n:
            print(f"i {i} | nums[i]: {nums[i]} | {nums}")
            if nums[i] in seen:
                nums.pop(i)
                n -= 1
                i -= 1
            else:
                seen.add(nums[i])
            
            i += 1
        
        return len(nums)