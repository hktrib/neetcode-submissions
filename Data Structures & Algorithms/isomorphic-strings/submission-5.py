class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_to_t = {}

        for i in range(len(s)):
            if s[i] in s_to_t and s_to_t[s[i]] != t[i]:
                return False
            s_to_t[s[i]] = t[i]

        freqS = Counter(s)
        freqT = Counter(t)

        for key, value in freqS.items():
            if freqT[s_to_t[key]] != value:
                return False

        # tempS = ""

        # for i in range(len(s)):
        #     tempS += s_to_t[s[i]]
        
        # if tempS == t:
        #     return True
        # else:
        #     return False

        return True