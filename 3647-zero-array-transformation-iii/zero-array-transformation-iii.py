class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort()
        available=SortedList() #maxHeap
        chosen=SortedList() #minHeap

        for i,num in enumerate(nums):
            while queries and queries[0][0]<=i:
                available.add(queries.pop(0)[1])
            while chosen and chosen[0]<i:
                chosen.pop(0)
            while num>len(chosen):
                if not available or available[-1]<i:
                    return -1
                chosen.add(available.pop())
        return len(available)