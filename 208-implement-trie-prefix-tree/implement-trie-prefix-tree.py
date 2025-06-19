class Node:
    def __init__(self):
        self.nei={}
        self.end=False

class Trie:
    def __init__(self):
        self.root=Node()

    def insert(self, word: str) -> None:
        cur=self.root
        for c in word:
            if c not in cur.nei:
                cur.nei[c]=Node()
            cur=cur.nei[c]
        cur.end=True

    def search(self, word: str) -> bool:
        cur=self.root
        for c in word:
            if c not in cur.nei:
                return False
            cur=cur.nei[c]
        return cur.end

    def startsWith(self, prefix: str) -> bool:
        cur=self.root
        for c in prefix:
            if c not in cur.nei:
                return False
            cur=cur.nei[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)