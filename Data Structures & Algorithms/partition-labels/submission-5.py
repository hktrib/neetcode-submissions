class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        final_pos = defaultdict()

        res = []

        for i, char in enumerate(s):
            if char in final_pos:
                final_pos[char] = i
            else:
                final_pos[char] = i

        start = 0
        last = 0
        for i, char in enumerate(s):
            last = max(final_pos[char], last)

            if i == last:
                res.append(last - start + 1)
                start = i + 1
                last = i + 1

        
        return res
