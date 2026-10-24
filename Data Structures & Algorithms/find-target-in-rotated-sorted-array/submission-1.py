class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        There are basically 2 sorted arrays split at one point
        
        For example:
        [3, 4, 5, 6, 1, 2]
        [3, 4, 5, 6] and [1, 2]

        How can we for example find 1 here?
        1. Get the middle element -> 5
        2. We have a limited number of cases to explore from

        [3, 4, 5 <--, 6, 1, 2]
         l     m            r
        * Here leftmost element > rightmost element, meaning that the right part might contain either elements < 3 or > 5
        while the left part will contain all elements between 3-5

        * We will choose to search for 1 in the right part:
        [6, 1, 2]
         l  m  r => found

         [6, 7, 1, 2, 3, 4, 5]
         
        '''

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1

        return -1
            