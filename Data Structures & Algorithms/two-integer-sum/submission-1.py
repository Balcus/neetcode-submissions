class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idxMap = {}
        seen = set()

        for i, n in enumerate(nums):
            need = target - n

            if need in seen:
                return [idxMap[need], i]

            seen.add(n)
            idxMap[n] = i
        
        return [-1, -1]