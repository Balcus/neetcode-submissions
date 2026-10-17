class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        res = []
        spaces = set(spaces)
        for i, c in enumerate(s):
            if i in spaces:
                res.append(' ')
            res.append(c)

        return "".join(res)