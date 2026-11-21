import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_heap = []
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

        for key, val in freq.items():
            heapq.heappush(max_heap, (-val, key))
        
        res = []
        for i in range(k):
            val, key = heapq.heappop(max_heap)
            res.append(key)
        
        return res