import random

def get_next_word(word, words_follow_dict):
    next_word = random.choice(words_follow_dict[word])
    return next_word

def check_stop_word(word):
    try:
        if word[-1] not in ["?", ".", "!"] and word[-2] not in ['?"', '!"', '."']:
            return False
        else:
            return True
    except IndexError:
        if word[-1] not in ["?", ".", "!"]:
            return False
        else:
            return True
# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
words_follow_dict = {}
words = words.split()
for i in range(len(words)-1):
    if words[i] in words_follow_dict:
        words_follow_dict[words[i]].append(words[i+1])
    else:
        words_follow_dict[words[i]] = [words[i+1]]

# TODO: construct 5 random sentences
for _ in range(5):
    start_words = [word for word in list(words_follow_dict.keys()) if word.istitle()]
    start_word = random.choice(start_words)
    sentence = start_word
    next_word = get_next_word(start_word, words_follow_dict)
    sentence += " " + next_word
    while not check_stop_word(next_word):
        next_word = get_next_word(next_word, words_follow_dict)
        sentence += " " + next_word
    print(sentence)

