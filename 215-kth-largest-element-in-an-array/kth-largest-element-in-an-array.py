class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        hp=[]
        for n in nums:
            heapq.heappush(hp,-n)
        i=0
        while i<k-1:
            heapq.heappop(hp)
            i+=1
        return -hp[0]