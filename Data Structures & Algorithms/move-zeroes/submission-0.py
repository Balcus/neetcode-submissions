class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums

        write, read = 0, 1
        while write < read and read < len(nums):
            if nums[read] != 0 and nums[write] == 0:
                nums[write] = nums[read]
                nums[read] = 0
                write += 1

            if nums[write] != 0 and write < read:
                write += 1

            read += 1
            

            