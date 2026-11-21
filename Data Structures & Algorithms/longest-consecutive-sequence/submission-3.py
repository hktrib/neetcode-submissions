class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cons = set(nums)
        
        maxLen = 0
        for num in cons:
            if num - 1 in cons:
                continue
            curr = num
            currLen = 0
            while curr in cons:
                currLen += 1
                curr += 1
            
            maxLen = max(maxLen, currLen)
        
        return maxLen