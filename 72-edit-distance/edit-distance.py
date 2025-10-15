class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1)<len(word2):
            word1,word2=word2,word1
        prev=list(range(len(word2)+1)) 
        for i,c1 in enumerate(word1,1):
            cur=[i]
            for j,c2 in enumerate(word2,1):
                if c1==c2:
                    cur.append(prev[j-1])
                else:
                    cur.append(1+min(prev[j],cur[-1],prev[j-1]))
            prev=cur
        return prev[-1]