class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        time = 0
        waitQ = deque()
        taskFreq = defaultdict(int)

        for task in tasks:
            taskFreq[task] += 1

        maxHeap = [(v, k) for k, v in taskFreq.items()]
        heapq.heapify_max(maxHeap)

        while maxHeap or waitQ:
            time += 1

            if maxHeap:
                freq, label = heapq.heappop_max(maxHeap)
                if freq - 1 > 0:
                    waitQ.append((time + n, freq - 1, label))

            while waitQ and waitQ[0][0] <= time:
                _, freq, label = waitQ.popleft()
                heapq.heappush_max(maxHeap, (freq, label))
        
        return time