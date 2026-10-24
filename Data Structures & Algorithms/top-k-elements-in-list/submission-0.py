class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = defaultdict(int)
        for n in nums:
            freqMap[n] += 1

        maxHeap = [(freq, num) for num, freq in freqMap.items()]
        heapq.heapify_max(maxHeap)

        res = []
        while k:
            _, n = heapq.heappop_max(maxHeap)
            res.append(n)
            k -= 1

        return res