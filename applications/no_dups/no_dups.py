def no_dups(s):
    cache = {}
    words = s.split()
    to_pop = []
    for i in range(len(words)):
        if words[i] in cache.keys():
            to_pop.append(i)
        else:
            cache[words[i]] = True
    to_pop.sort(reverse=True)
    for value in to_pop:
        words.pop(value)
    return " ".join(words)

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))