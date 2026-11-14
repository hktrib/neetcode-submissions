class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening_braces = "([{"

        for char in s:
            if char not in opening_braces:
                if stack:
                    match char: 
                        case ")":
                            if stack[-1] == "(":
                                stack.pop()
                            else:
                                return False
                        case "]":
                            if stack[-1] == "[":
                                stack.pop()
                            else:
                                return False
                        case "}":
                            if stack[-1] == "{":
                                stack.pop()
                            else:
                                return False
                        case _:
                            continue
                else:
                    return False
            else:
                stack.append(char)

        return False if stack else True
