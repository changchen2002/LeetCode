class StockSpanner:

    def __init__(self):
        self.dec=[]

    def next(self, price: int) -> int:
        res=1        
        while self.dec and price>=self.dec[-1][0]:
            res+=self.dec.pop()[1]
        self.dec.append((price,res))
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)