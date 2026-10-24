class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap, tMap = defaultdict(int), defaultdict(int)

        for c in s:
            sMap[c] += 1

        for c in t:
            tMap[c] += 1
        
        return sMap == tMap