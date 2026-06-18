class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freqList = dict()

        res = 0
        resCount = 0

        for num in nums:
            freqList[num] = 1 + freqList.get(num, 0)
            if freqList[num] >= resCount:
                res = num 
                resCount = freqList[num]
        return res
