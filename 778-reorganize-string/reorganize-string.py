import heapq
from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        count=Counter(s)
        maxHeap=[(-cnt,c)for c, cnt in count.items()]
        heapq.heapify(maxHeap)

        result=[]
        prev=(0,"")
        while maxHeap:
            freq,c=heapq.heappop(maxHeap)
            result.append(c)
            if prev[0]<0:
                heapq.heappush(maxHeap,prev)
            prev=(freq+1,c)
        return "".join(result) if len(result)==len(s) else ""