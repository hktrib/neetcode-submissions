class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        l = 0
        r = 0

        abbrLength = 0

        i = 0
        j = 0
        while i < len(word) and j < len(abbr):
            print(f"i : {i} j: {j} | word[i]: {word[i]} abbr[j]: {abbr[j]}")

            start = j
            if abbr[start] == "0":
                return False
            while j < len(abbr) and abbr[j].isdigit():
                j += 1
            
            if j != start:
                num = int(abbr[start: j])
                print(f"num: {num}")

                if i + num > len(word):
                    return False
                else:
                    i += num
            else:
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
        

        return i == len(word) and j == len(abbr)