class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0

        current_seen = defaultdict(int)

        longest = 0
        for r in range(len(s)):
            # should catch the very first duplicate
            if s[r] not in current_seen:
                longest = max(longest, r - l + 1)
                current_seen[s[r]] += 1
            else:
                while s[r] in current_seen:
                    # simply delete from current_seen
                    del current_seen[s[l]]
                    l += 1

                current_seen[s[r]] = 1

        return longest