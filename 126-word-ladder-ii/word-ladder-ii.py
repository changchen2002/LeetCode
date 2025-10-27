class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet=set(wordList)
        if endWord not in wordSet: return []
        
        layer={beginWord}
        parents=defaultdict(set)
        while layer and endWord not in parents:
            new_layer=defaultdict(set)
            for w in layer:                
                for i in range(len(w)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        nxt = w[:i] + c + w[i+1:]
                        if nxt in wordSet:
                            new_layer[nxt].add(w)
            wordSet-=set(new_layer.keys())
            layer=new_layer
            for k,v in new_layer.items():
                parents[k]|=v 
        
        res=[]
        def backtrack(word,path):
            if word==beginWord:
                res.append(path[::-1])
                return
            for p in parents[word]:
                backtrack(p,path+[p])
            
        if endWord in parents:
            backtrack(endWord,[endWord])
        return res
