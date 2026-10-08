class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        def dfs(i, cur):
            if i >= len(nums):
                res.append(cur[:])
                return

            for n in nums:
                if n not in cur:
                    cur.append(n)
                    dfs(i + 1, cur)
                    cur.pop()

        dfs(0, [])
        return res