class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = {}

        for s in strs:
            key = tuple(sorted(s))
            if key not in anagramMap:
                anagramMap[key] = [s]
            else:
                anagramMap[key].append(s)

        return [v for v in anagramMap.values()]