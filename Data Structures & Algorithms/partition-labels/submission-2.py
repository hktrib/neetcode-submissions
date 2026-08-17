class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        first_and_last = defaultdict()

        res = []

        for i, char in enumerate(s):
            if char in first_and_last:
                first_and_last[char][1] = i
            else:
                first_and_last[char] = [i, i]

        start = 0
        last = 0
        for i, char in enumerate(s):
            last = max(first_and_last[char][1], last)

            if i == last:
                res.append(last - start + 1)
                start = i + 1
                last = i + 1

        
        return res
