class Solution:
    def isPalindrome(self, s: str) -> bool:
        return self.checkPalindrome(s, 0, len(s) - 1)
        

    def checkPalindrome(self, s, l, r) -> bool:
        if l > r:
            return True
        elif not s[l].isalnum():
            return self.checkPalindrome(s, l + 1, r)
        elif not s[r].isalnum():
            return self.checkPalindrome(s, l, r - 1)
        elif s[l].lower() == s[r].lower():
                return self.checkPalindrome(s, l + 1, r - 1)
        else:
            return False
