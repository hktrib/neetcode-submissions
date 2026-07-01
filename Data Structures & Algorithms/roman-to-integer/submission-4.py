class Solution:
    def romanToInt(self, s: str) -> int:
        hm = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }

        total = 0
        i = 0
        while i < len(s):
            print(f"i = {i} | total = {total}")
            curr_val = hm[s[i]]

            if i + 1 < len(s) and s[i + 1] in hm and hm[s[i + 1]] > curr_val:
                print(f"curr = {s[i : i + 2]}")
                curr_val = hm[s[i : i + 2]]
                i += 1

            i += 1
            total += curr_val
        
        return total