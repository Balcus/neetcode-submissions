class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.left, num)

        if self.left and self.right and self.left[0] > self.right[0]:
            n = heapq.heappop_max(self.left)
            heapq.heappush(self.right, n)

        if len(self.left) > len(self.right) + 1:
            n = heapq.heappop_max(self.left)
            heapq.heappush(self.right, n)

        if len(self.right) > len(self.left) + 1:
            n = heapq.heappop(self.right)
            heapq.heappush_max(self.left, n)

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (self.left[0] + self.right[0]) / 2
        if len(self.left) > len(self.right):
            return self.left[0]
        else:
            return self.right[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()