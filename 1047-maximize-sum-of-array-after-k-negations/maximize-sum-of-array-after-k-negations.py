class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while k>0:
            top=heapq.heappop(nums)
            heapq.heappush(nums,-top)
            k-=1
        return sum(nums)