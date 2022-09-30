#Did you mean ...?

import difflib
class Dictionary:
    def __init__(self,words):
        self.words=words
    def find_most_similar(self,term):
        collections = {}
        for word in self.words:
            ret = difflib.SequenceMatcher(None, word, term).ratio()
            collections[word] = ret
        print(collections)
        return sorted(collections.items(), key=lambda x: x[1])[-1][0]

words = ['codewars', 'code', 'stars', 'wars', 'codec', 'mars']
a = Dictionary(words)

print(a.find_most_similar('coddwars'))