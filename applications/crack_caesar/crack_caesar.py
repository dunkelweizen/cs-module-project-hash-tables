with open("ciphertext.txt") as f:
    words = f.read()
char_dict = {}
for char in words:
    if char in char_dict.keys():
        char_dict[char] += 1
    else:
        char_dict[char] = 1
freq_list = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

list_dict = list(char_dict.items())
list_dict.sort(reverse=True, key=lambda pair: pair[1])

list_dict = [x for x in list_dict if x[0].isalpha()]

conversion_dict = {}

for i in range(len(freq_list)):
    conversion_dict[list_dict[i][0]] = freq_list[i]


result = ""
for char in words:
    try:
        convert_char = conversion_dict[char]
        result += convert_char
    except KeyError:
        result += char

print(result)