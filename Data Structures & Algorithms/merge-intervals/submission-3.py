class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        res = []
        res.append(intervals[0])
        prev = intervals[0][1]

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if start > prev :
                res.append([start, end])
                prev = end
                continue

            prev = max(prev, end)
            res[-1][1] = prev

        return res