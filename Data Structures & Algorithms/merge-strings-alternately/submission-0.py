class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1 = 0
        w2 = 0

        flag = False

        res = []

        while w1 < len(word1) and w2 < len(word2):
            if not flag:
                res.append(word1[w1])
                w1 += 1
                flag = True
            else:
                res.append(word2[w2])
                w2 += 1
                flag = False

        
        if w1 != len(word1):
            res.append(word1[w1:])
        else:
            res.append(word2[w2:])

        return "".join(res)
        