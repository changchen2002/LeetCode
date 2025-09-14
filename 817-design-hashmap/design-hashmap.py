class MyHashMap:
    def __init__(self):
        self.base=769
        self.buckets=[[] for _ in range(self.base)]

    def _hash(self,key):
        return key%self.base

    def put(self, key: int, value: int) -> None:
        h=self._hash(key)
        for i, (k,v) in enumerate(self.buckets[h]):
            if k==key:
                self.buckets[h][i]=(key,value)
                return
        self.buckets[h].append((key,value))

    def get(self, key: int) -> int:
        h=self._hash(key)
        for k,v in self.buckets[h]:
            if k==key:
                return v
        return -1

    def remove(self, key: int) -> None:
        h=self._hash(key)
        for i, (k,v) in enumerate(self.buckets[h]):
            if k==key:
                self.buckets[h].pop(i)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)