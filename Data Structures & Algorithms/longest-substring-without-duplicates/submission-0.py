class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        seen = set()
        start = end = 0
        maxLen = 0

        while end < len(s):
            if s[end] not in seen:
                seen.add(s[end])
                end += 1
            else:
                seen.remove(s[start])
                start += 1
            maxLen = max(maxLen, end - start)

        return maxLen