class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet=set(wordList)
        if endWord not in wordList:
            return 0
        
        q=deque([(beginWord,1)])
        while q:
            word,step=q.popleft()
            if word==endWord:
                return step
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    nxt=word[:i]+c+word[i+1:]
                    if nxt in wordSet:
                        q.append([nxt,step+1])
                        wordSet.remove(nxt) 
        
        return 0