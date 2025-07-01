class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq=list(Counter(tasks).values())
        f_max=max(freq)
        maxCount=freq.count(f_max)
        return max(len(tasks),(f_max-1)*(n+1)+maxCount)
