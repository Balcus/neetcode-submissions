class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        dedup = set(nums)

        for n in nums:
            if n - 1 in dedup:
                continue
            else:
                count = 1
                nxt = n + 1
                while nxt in dedup:
                    count += 1
                    nxt += 1
                if count > res:
                    res = count
        
        return res