class MedianFinder:

    def __init__(self):
        self.minHp=[]
        self.maxHp=[]

    def addNum(self, num: int) -> None:
        if not self.maxHp:
            heapq.heappush(self.maxHp,-num)
        elif num>-(self.maxHp[0]):
            heapq.heappush(self.minHp,num)
        else:
            heapq.heappush(self.maxHp,-num)
        
        if len(self.maxHp)>len(self.minHp)+1:
            n=-heapq.heappop(self.maxHp)
            heapq.heappush(self.minHp,n)
        elif len(self.minHp)>len(self.maxHp)+1:
            n=heapq.heappop(self.minHp)
            heapq.heappush(self.maxHp,-n)

    def findMedian(self) -> float:
        if len(self.maxHp)==len(self.minHp):
            return (-self.maxHp[0]+self.minHp[0])/2
        elif len(self.maxHp)>len(self.minHp):
            return -self.maxHp[0]
        else:
            return self.minHp[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

