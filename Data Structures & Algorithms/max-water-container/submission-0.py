class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0
        while l <= r:
            left = heights[l]
            right = heights[r]
            area = min(left, right) * (r - l)
            res = max(res, area)

            if left < right:
                l += 1
            else:
                r -= 1
        return res