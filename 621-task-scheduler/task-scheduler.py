class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=Counter(tasks)
        maxFreq=0
        maxCount=0
        for task,freq in count.items():
            maxFreq=max(maxFreq,freq)
        for task,freq in count.items():
            if freq==maxFreq:
                maxCount+=1
        return max((maxFreq-1)*(n+1)+maxCount,len(tasks))

