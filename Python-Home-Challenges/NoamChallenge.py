
with open('sample.txt', 'r') as file:
    data = file.read().replace('\n', '')
    print("The content of the file is:\n\n" + data)


import re
words = re.sub("[^\w]", " ",  data).split()

for word in words:
	from collections import Counter
	word_counts = Counter(words)

MOword = word_counts.most_common(1)[0][0]
MOtimes = word_counts.most_common(1)[0][1]

print("\nThe most occuring word is {} and it occurs {} times".format(MOword,MOtimes))


