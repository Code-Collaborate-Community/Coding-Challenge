f = open("Challenge_01.txt", "r")
data = f.read().split()
dict = {}
for word in data:
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1
print(
    f'Most recurring word in that file: {max(dict, key=dict.get)}, And it appears {dict[max(dict, key=dict.get)]} times')
