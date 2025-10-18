class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        c2p=sorted(zip(capital,profits))
        i=0
        max_heap=[]
        while k>0:
            while i<len(capital) and c2p[i][0]<=w:
                heapq.heappush(max_heap,-c2p[i][1])
                i+=1
            if not max_heap:
                break
            w-=heapq.heappop(max_heap)
            k-=1

        return w
