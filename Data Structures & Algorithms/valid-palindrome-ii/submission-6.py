class Solution:
    def validPalindrome(self, s: str) -> bool:
        aparadhas = 0

        s = "".join(ch for ch in s if ch.isalnum()).lower()

        l = 0
        r = len(s) - 1


        def helper(inside: str) -> bool:
            left = 0
            right = len(inside) - 1

            while left <= right:
                if inside[left] != inside[right]:
                    return False
                left += 1
                right -= 1
            
            return True

        while l <= r:
            if s[l] != s[r]:
                skipLeft = helper(s[l + 1 : r + 1])
                skipRight = helper(s[l : r])
                return skipLeft or skipRight

            l += 1
            r -= 1

        
        return True if aparadhas <= 1 else False