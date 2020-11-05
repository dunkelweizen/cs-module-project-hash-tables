import sys
sys.path.append('../')
from word_count.word_count import word_count

with open("robin.txt") as f:
    words = f.read()

for word in words:
    word = word.lower()

word_dict = word_count(words)
longest = 0
for word in word_dict.keys():
    if len(word) > longest:
        longest = len(word)
        longest_word = word
longest = longest + 2
list_dict = list(word_dict.items())
list_dict.sort(reverse=True, key=lambda pair: pair[1])

for key, value in list_dict:
    spaces = longest - len(key)
    print(key, spaces * " ", value * '#')