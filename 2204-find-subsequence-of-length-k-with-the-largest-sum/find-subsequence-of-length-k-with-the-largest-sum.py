class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        maxHeap=[]
        for i,num in enumerate(nums):
            heapq.heappush(maxHeap,(-num,i))
        minHeap=[]
        for _ in range(k):
            num,i=heapq.heappop(maxHeap)
            heapq.heappush(minHeap,(i,-num))
        res=[]
        for _ in range(k):
            i,num=heapq.heappop(minHeap)
            res.append(num)
        return res