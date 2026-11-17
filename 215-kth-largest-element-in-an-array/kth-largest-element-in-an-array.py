class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        hp=[]
        for num in nums:
            heapq.heappush(hp,num)
            if hp and len(hp)>k:
                heapq.heappop(hp)
        return hp[0]