class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        max_sum = float('-inf')
        for n in nums:
            cur_sum += n
            max_sum = max(max_sum, cur_sum)

            if cur_sum < 0:
                cur_sum = 0
        return max_sum