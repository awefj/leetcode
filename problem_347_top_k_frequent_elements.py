import collections
import heapq
from typing import List


class Solution:
    def topKFrequent01(self, nums: List[int], k: int) -> List[int]:
        freq = collections.Counter(nums)
        heap = []
        for f in freq:
            heapq.heappush(heap, (-freq[f], f))
        top_k = list()
        for _ in range(k):
            top_k.append(heapq.heappop(heap)[1])
        return top_k

    def topKFrequent02(self, nums: List[int], k: int) -> List[int]:
        return list(zip(*collections.Counter(nums).most_common(k)))[0]
