class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = defaultdict(int)
        most_freq_char = 0

        l = 0
        longest = 0

        # most_freq_char not being updated is not a problem
        # this just stops any future windows which have a length 
        # less than most_freq_char from expanding past old_max_size
        for r in range(len(s)):
            window[s[r]] += 1
            most_freq_char = max(most_freq_char, window[s[r]])

            if (r - l + 1) - most_freq_char <= k:
                longest = max(longest, (r - l + 1))
            else:
                while (r - l + 1) - most_freq_char > k:
                    window[s[l]] -= 1
                    if window[s[l]] == 0:
                        del window[s[l]]
                    l += 1
                    # most_freq_char = max(window.values())
            
        return longest