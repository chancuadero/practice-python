from collections import Counter
from .token_utils import tokenize, filter_word_counts

class Document:
    def __init__(self, text):
        self.text = text
        #pre tokenize the document with non-public tokenize method
        self.tokens = self._tokenize()
        #pre tokenize the document with non-public tokenize method
        self.word_counts = self._count_words()

    def _tokenize(self):
        return tokenize(self.text)
    
    def _count_words(self):
        return Counter(self.tokens)
    
class SocialMedia(Document):
    def __init__(self, text):
        Document.__init__(self, text)
        self.hashtag_counts = self._count_hashtags()
        self.mention_counts = self._count_mentions()

    def _count_hashtags(self):
        # Filter attribute so only words starting with '#' remain
        return filter_word_counts(self.word_counts, first_char='#')      

    def _count_mentions(self):
        # Filter attribute so only words starting with '@' remain
        return filter_word_counts(self.word_counts, first_char='@')