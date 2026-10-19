class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            c = s[i]
            if c == '*':
                stack.pop()
            else:
                stack.append(c)

        return "".join(stack)
