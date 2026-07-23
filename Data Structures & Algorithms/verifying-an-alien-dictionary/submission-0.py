class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) == 1:
            return True
        
        mapping = dict()

        for i, char in enumerate(order):
            mapping[char] = i

        def inOrder(word1, word2) -> bool:
            l, r = 0, 0
            while l < len(word1) and r < len(word2):
                lpos, rpos = mapping[word1[l]], mapping[word2[r]]
                
                if lpos < rpos:
                    return True
                if lpos > rpos:
                    return False

                l += 1
                r += 1

            return len(word1) <= len(word2)

            pass

        l = 0
        r = 1

        while r < len(words): 
            res = inOrder(words[l], words[r])
            if not res:
                return False
            l += 1
            r += 1
        
        return True
        
