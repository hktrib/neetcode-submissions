from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        return list(map(lambda x: x[0], freq.most_common(k)))

