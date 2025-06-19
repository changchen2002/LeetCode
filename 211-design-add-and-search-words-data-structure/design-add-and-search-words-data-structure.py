class Node:
    def __init__(self):
        self.nei={}
        self.end=False

class WordDictionary:

    def __init__(self):
        self.root=Node()

    def addWord(self, word: str) -> None:
        cur=self.root
        for c in word:
            if c not in cur.nei:
                cur.nei[c]=Node()
            cur=cur.nei[c]
        cur.end=True

    def search(self, word: str) -> bool:
        cur=self.root

        def dfs(i,cur):
            if i==len(word):
                return cur.end
            if word[i]=='.':
                for nei in cur.nei.values():
                    if dfs(i+1,nei):
                        return True
                return False
            if word[i] not in cur.nei:
                return False
            return dfs(i+1,cur.nei[word[i]])
        return dfs(0,cur)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)