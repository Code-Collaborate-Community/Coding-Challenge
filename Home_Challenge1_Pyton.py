file = open("C:/Users/tomer/PycharmProjects/HomeChallenge3/Readme.txt")
words = open("C:/Users/tomer/PycharmProjects/HomeChallenge3/Readme.txt").read().split()

print(file.read())
print(words)


def keywithmaxval(d):
    """ a) create a list of the dict's keys and values;
        b) return the key with the max value"""
    v = list(d.values())
    k = list(d.keys())
    return k[v.index(max(v))]


def word_count(words):
    counts = dict()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return keywithmaxval(counts), max(counts.values())


print("max word is:", (word_count(words)))
print(file.read())
file.close()
