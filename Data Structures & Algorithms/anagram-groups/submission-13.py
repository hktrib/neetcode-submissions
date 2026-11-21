from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_mapper = defaultdict(list)
        res = []

        for i in range(len(strs)):
            # anagram_mapper[strs[i]] = "".join(sorted(strs[i]))
            sortedVal = "".join(sorted(strs[i]))
            anagram_mapper[sortedVal].append(strs[i])
        

        return list(anagram_mapper.values())
