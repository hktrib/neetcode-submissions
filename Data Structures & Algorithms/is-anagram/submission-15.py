from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = Counter(s)
        tMaps = Counter(t)
        return sMap == tMaps