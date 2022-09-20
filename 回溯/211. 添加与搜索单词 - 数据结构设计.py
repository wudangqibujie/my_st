class WordDictionary(object):

    def __init__(self):
        self.trie = dict()


    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        self.add(0, word, self.trie)

    def add(self, chr_ix, word, trie):
        if chr_ix >= len(word):
            return
        if word[chr_ix] not in trie:
            trie[word[chr_ix]] = dict()
        self.add(chr_ix + 1, word, trie[word[chr_ix]])

    def find(self, chr_ix, word, trie):
        if chr_ix >= len(word):
            return True
        rslt = []
        if word[chr_ix] == ".":
            keys = trie.keys()
            for k in keys:
                rslt.append(self.find(chr_ix + 1, word, trie[k]))
            return any(rslt)
        if word[chr_ix] not in trie:
            return False
        return self.find(chr_ix + 1, word, trie[word[chr_ix]])

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if not word:
            return False

        return self.find(0, word, self.trie)


w = WordDictionary()
w.addWord("bad")
w.addWord("dad")
w.addWord("mad")
print(w.search(""))
print(w.search("."))
print(w.search("pad"))
print(w.search("bad"))
print(w.search(".ad"))
print(w.search("b."))