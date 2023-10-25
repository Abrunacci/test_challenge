import math
import os
import random
import re
import sys

#
# Complete the 'stop_words' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING text
#  2. INTEGER k
#
from collections import Counter, OrderedDict


def stopWords(text, k):
    # Write your code here
    splitted_text = text.lower().split()
    c = Counter(splitted_text)
    c = OrderedDict(c.most_common())
    stop_words = set()
    for word, count in c.items():
        if count >= k:
            stop_words.add(word)
    response = OrderedDict()
    for index, word in enumerate(splitted_text):
        if word in stop_words and word not in response.items():
            response[word] = index

    return [key for key in response.keys()]
