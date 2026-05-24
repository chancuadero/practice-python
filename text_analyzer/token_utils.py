import re
from collections import Counter

def filter_word_counts(word_counts, first_char):
    """Filters a Counter/dict of words by their starting character."""
    # 1. Filter the items into a normal dictionary
    filtered_dict = {word: count for word, count in word_counts.items() if word.startswith(first_char)}
    
    # 2. FIXED: Wrap the dictionary in a Counter so .most_common() works!
    return Counter(filtered_dict)

def tokenize(text):
    return re.findall(r"[@#]\w+|\w+", text)