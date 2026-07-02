class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nBy3 = n // 3

        print(nBy3)

        allNums = Counter(nums)

        res = []

        for key, value in allNums.items():
            if value > nBy3:
                res.append(key)
        
        return res
