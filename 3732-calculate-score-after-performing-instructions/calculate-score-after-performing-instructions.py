class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        res=i=0
        hashset=set()
        while 0<=i<len(values):
            if i in hashset:
                return res
            hashset.add(i)
            if instructions[i]=="jump":
                i=values[i]+i
            elif instructions[i]=="add":
                res+=values[i]
                i+=1        
        return res
