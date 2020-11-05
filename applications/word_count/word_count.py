forbidden_symbols = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'.split()
def word_count(s):
    words = s.split()
    words = [word.lower() for word in words]
    word_dict = {}
    for word in words:
        if all(char in forbidden_symbols for char in word):
            continue
        if not all(char.isalpha() for char in word):
            chars = [char for char in word if char not in forbidden_symbols]
            word = ''.join(chars)
        if word in word_dict.keys():
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict




if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))