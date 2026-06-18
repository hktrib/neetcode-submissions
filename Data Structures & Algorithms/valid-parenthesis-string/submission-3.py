class Solution:
    def checkValidString(self, s: str) -> bool:
        
        # l = 0
        # r = len(s) - 1


        # while l <= r:


        minOpen = 0
        maxOpen = 0

        for i in range(len(s)):
            match s[i]:
                case "(":
                    minOpen += 1
                    maxOpen += 1
                case ")":
                    minOpen -= 1
                    maxOpen -= 1
                case "*":
                    minOpen -= 1
                    maxOpen += 1
            
            if minOpen < 0:
                minOpen = 0
            
            if maxOpen < 0:
                return False
        
        if minOpen == 0:
            return True
        else:
            return False