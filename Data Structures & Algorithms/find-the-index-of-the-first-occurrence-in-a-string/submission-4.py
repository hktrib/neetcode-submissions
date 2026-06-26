class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        l = 0
        r = len(needle) - 1
        while r < len(haystack):
            print(haystack[l:r + 1])
            if needle == haystack[l:r + 1]:
                return l
            else:
                l += 1
                r += 1
        
    
        return -1