class StockSpanner:

    def __init__(self):
        self.dec=[]
        self.hashmap={}

    def next(self, price: int) -> int:
        res=1        
        while self.dec and price>=self.dec[-1]:
            prev=self.dec.pop()
            res+=self.hashmap[prev]
        self.dec.append(price)
        self.hashmap[price]=res
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)