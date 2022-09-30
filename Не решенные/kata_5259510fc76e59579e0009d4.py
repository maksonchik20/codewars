import difflib
class Dictionary:
    def __init__(self,words):
        self.words=words
    def find_most_similar(self,term):
        collections = {}
        for word in self.words:
            ret = difflib.SequenceMatcher(None, word, term).get_matching_blocks()
            collections[word] = len(word) - len(term) -  sum([i[2] for i in ret])
        return sorted(collections.items(), key=lambda x: x[1])[0][0]

words = ['cherry', 'peach', 'pineapple', 'melon', 'strawberry', 'raspberry', 'apple', 'coconut', 'banana']
a = Dictionary(words)

print(a.find_most_similar('strawbery'))