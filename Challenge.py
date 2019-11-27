from collections import Counter

f = open("text.txt", "r")
if f.mode == 'r':
    contents = f.read().split()
    print(contents)

word_count = Counter(contents)
print(word_count.most_common(1))



