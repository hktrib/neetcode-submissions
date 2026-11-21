class Solution:
    def isPalindrome(self, s: str) -> bool:
        def checkPalindrome(s, l, r) -> bool:
            if l > r:
                return True
            elif not s[l].isalnum():
                return checkPalindrome(s, l + 1, r)
            elif not s[r].isalnum():
                return checkPalindrome(s, l, r - 1)
            elif s[l].lower() == s[r].lower():
                return checkPalindrome(s, l + 1, r - 1)
            else:
                return False
        return checkPalindrome(s, 0, len(s) - 1)
        

