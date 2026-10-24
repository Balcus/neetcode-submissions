class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start, end = 0, 0
        count = defaultdict(int)
        maxf = 0
        res = 1

        while end < len(s):
            count[s[end]] += 1
            maxf = max(maxf, count[s[end]])

            while end - start + 1 - maxf > k:
                count[s[start]] -= 1
                start += 1
            
            res = max(res, end - start + 1)
            end += 1
        
        return res