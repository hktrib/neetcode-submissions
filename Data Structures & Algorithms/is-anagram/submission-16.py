from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return Counter(s) == Counter(t)

        sMap = dict()
        tMap = dict()

        for char in s:
            sMap[char] = sMap.get(char, 0) + 1
        for char in t:
            tMap[char] = tMap.get(char, 0) + 1

        for key, value in sMap.items():
            if key in tMap and tMap[key] == value:
               continue
            else:
                return False
        
        return len(tMap) == len(sMap)