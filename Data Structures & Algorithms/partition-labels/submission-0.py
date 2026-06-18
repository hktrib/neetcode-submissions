class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        freq = {}
        
        for char in s:
            freq[char] = 1 + freq.get(char, 0)

        
        res = []
        l = 0
        r = 0
        k = 0
        while r < len(s):
            print(freq)
            print(f"s[r] {s[r]} | r -> {r} | k")
            k += freq.pop(s[r])

            while r < k:
                if s[r] in freq:
                    k += freq.pop(s[r])
                r += 1
            
            res.append(r - l)
            l = r

        return res
