class Trie:

    def __init__(self):
        pass

    def insert(self, word):
        pass

    def search(self, word):
        pass

    def startsWith(self, prefix):
        pass

trie = Trie()
trie.insert("apple")
trie.insert("app")
print(trie.startsWith("apple"))
print(trie.search("app"))

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)