class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = strs[0]

        for i, s in enumerate(strs):
            lcp = lcp[:len(s)]
            for j in range(len(lcp)):
                if s[j] != lcp[j]:
                    lcp = lcp[:j]
                    break
                
            if not lcp:
                break

        return lcp
