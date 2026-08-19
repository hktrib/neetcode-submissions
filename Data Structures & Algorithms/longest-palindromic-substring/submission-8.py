class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = [0, 0]
        resLen = 0

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = [l, r + 1]
                    resLen = r - l + 1

                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = [l, r + 1]
                    resLen = r - l + 1

                l -= 1
                r += 1
        
        return s[res[0]: res[1]]