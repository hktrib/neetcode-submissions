class Solution:
    def maxScore(self, s: str) -> int:
        
        leftPrefix = [0] * len(s)
        rightPrefix = [0] * len(s)

        zeroes = 0
        ones = 0

        for i in range(len(leftPrefix)):
            if s[i] == "0":
                zeroes += 1
            leftPrefix[i] = zeroes
        
        for i in range(len(rightPrefix) - 1, -1, -1):
            if s[i] == "1":
                ones += 1
            rightPrefix[i] = ones

        print(f"leftPrefix = {leftPrefix}")
        print(f"rightPrefix = {rightPrefix}")

        maxScore = leftPrefix[0] + rightPrefix[1]

        print(f"maxScore : {maxScore}")
        for i in range(1, len(s)):
            maxScore = max(leftPrefix[i - 1] + rightPrefix[i], maxScore)
        
        return maxScore

