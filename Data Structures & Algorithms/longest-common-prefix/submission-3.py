class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        smallest = strs[0]

        for i in range(len(strs)):
            lcp = ""
            if strs[i] == lcp:
                return lcp
            for j in range(len(strs[i])):
                if j < len(smallest) and strs[i][j] == smallest[j]:
                    lcp += smallest[j]
                else:
                    break
            smallest = lcp

            print(smallest)
        
        return smallest
                

        
