class Logger:

    def __init__(self):
        self.time=0
        self.hashmap={}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        
        if message in self.hashmap.keys():
            if timestamp>=self.hashmap[message]:
                self.hashmap[message]=timestamp+10
                return True
            else:
                return False
        else:
            self.hashmap[message]=timestamp+10
            return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)