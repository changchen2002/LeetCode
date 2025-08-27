class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort()
        idx=0
        available=[] #maxHeap
        chosen=[] #minHeap

        for i,num in enumerate(nums):
            while idx<len(queries) and queries[idx][0]<=i:
                heapq.heappush(available,-queries[idx][1])
                idx+=1
            while chosen and chosen[0]<i:
                heapq.heappop(chosen)
            while num>len(chosen):
                if not available or -available[0]<i:
                    return -1
                top=-heapq.heappop(available)
                heapq.heappush(chosen,top)

        return len(available)