class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tMap = Counter(t)
        curMap = defaultdict(int)
        need = len(tMap.keys())
        have = 0
        start, end = 0, 0
        res = (-1, -1)

        for end in range(len(s)):
            curMap[s[end]] += 1
            if curMap[s[end]] == tMap.get(s[end], -1):
                have += 1

            while have == need:
                i, j = res
                if i == -1 or end - start + 1 < j - i + 1:
                    res = (start, end)

                curMap[s[start]] -= 1

                if curMap[s[start]] < tMap.get(s[start], 0):
                    have -= 1
                start += 1

        i, j = res
        return s[i: j + 1] if i != -1 and j != -1 else ""
                
