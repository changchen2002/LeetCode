class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers=sorted([(w/q,q) for q,w in zip(quality,wage)])
        res=float('inf')
        total=0
        max_heap=[]

        for ratio,q in workers:
            heapq.heappush(max_heap,-q)
            total+=q
            if len(max_heap)>k:
                total+=heapq.heappop(max_heap)
            if len(max_heap)==k:
                res=min(res,total*ratio)
        return res

# quality = [10,20,5]
# wage = [70,50,30]
# k = 2
# •	计算 ratio: [7.0, 2.5, 6.0]
# •	排序后：
# [(2.5,20), (6.0,5), (7.0,10)]
# •	依次计算最小总花费：
# → 105.0
