from collections import Counter

func = open("Hallelujah.txt", "r")
if func.mode == 'r':
    contents = func.read().split()
    print(contents)

wordsCount = Counter(contents)
print(wordsCount.most_common(1))