from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # basically here we want to get a window of the size
        # of the smaller string min(s1, s2) and the get its character
        # frequency


        # since we know the length of that string we fix a window of that size
        # and march down the other string with a running char freq to compare with
        # we are looking for when the 2 character frequencies match


        # one optimization we can do here when matching character frequencies instead
        # looping across both dictionaries is to keep a count variable than only gets
        # incremented when the running_window has got a character equal to the original characters frequency

        # when these two counts match, we know we got a hit


        # else if they don't match....anyways lets build to this

        bs = ""
        cs = ""
        if len(s1) <= len(s2):
            bs = s1
            cs = s2
        else:
            bs = s2
            cs = s1

        base_window = defaultdict(int)
        for char in s1:
            base_window[char] += 1
    
        l = r = 0
        base_count, new_count = len(base_window), 0
        new_window = defaultdict(int)

        print(f"base_count {base_count}")
        print(f"base_window {base_window}")
        print(f"new_count {new_count}")
        for r in range(len(cs)):
            new_window[cs[r]] += 1
            if cs[r] in base_window and new_window[cs[r]] == base_window[cs[r]]:
                new_count += 1

            print(f"1. new_window {new_window}")
            print(f"1. new_count {new_count}")

            while (r - l + 1) > len(bs):
                if cs[l] in base_window and base_window[cs[l]] == new_window[cs[l]]:
                    new_count -= 1

                new_window[cs[l]] -= 1
                l += 1
                pass

            print(f"2. new_window {new_window}")
            print(f"2. new_count {new_count}")

            if new_count == base_count:
                return True
        
        return False
            


        