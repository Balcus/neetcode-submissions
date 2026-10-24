class Solution:
    def isValid(self, s: str) -> bool:
        opening = [ '(', '[', '{' ]
        stack = []
        for c in s:
            if c in opening:
                stack.append(c)
            else:
                if not stack:
                    return False
                top = stack[-1]
                if (top == '(' and c == ')') or (top == '[' and c == ']') or (top == '{' and c == '}'):
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
