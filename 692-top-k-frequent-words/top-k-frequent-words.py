class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count=Counter(words)
        bucket=[[] for _ in range(1,len(words)+1)]  #possible frequency
        for w,freq in count.items():
            bucket[freq].append(w)    
        res=[]
        for i in range(len(bucket)-1,-1,-1):
            bucket[i].sort()
            for n in bucket[i]:
                if k>0:
                    res.append(n)
                    k-=1
        return res