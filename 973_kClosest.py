class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for i,j in points:
            d = (i ** 2) + ( j ** 2)
            minHeap.append([d, i, j])
        heapq.heapify(minHeap)
        output = []
        while k > 0:
            d, i, j = heapq.heappop(minHeap)
            output.append([i, j])
            k -= 1
        return output