class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        hp=[]

        for n in nums:
            heapq.heappush(hp,n)
            while len(hp)>k:
                heapq.heappop(hp)
        return hp[0]