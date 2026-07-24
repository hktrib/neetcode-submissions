class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adjList = dict()

        for i in range (1, n + 1):
            adjList[i] = set()

        for ai, bi, in trust:
            adjList[ai].add(bi)
        
        candidates = set()

        for key, values in adjList.items():
            if len(values) == 0:
                candidates.add(key)
        
        print(candidates)

        final_candidates = set()

        for candidate in candidates:
            flag = True
            for key, values in adjList.items():
                if key == candidate:
                    continue
                else:
                    if candidate not in values:
                        flag = False
                        break
            if flag:
                final_candidates.add(candidate)
        
        if len(final_candidates) == 1:
            return final_candidates.pop()
        else:
            return -1