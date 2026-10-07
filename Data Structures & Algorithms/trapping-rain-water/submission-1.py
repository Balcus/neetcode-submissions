class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxLeft, maxRight = height[l], height[r]
        total = 0

        while l < r:
            if maxLeft < maxRight:
                s = maxLeft - height[l]
                if s > 0:
                    total += s
                l += 1
                maxLeft = max(maxLeft, height[l])
            else:
                s = maxRight - height[r]
                if s > 0:
                    total += s
                r -= 1
                maxRight = max(maxRight, height[r])

        return total

        