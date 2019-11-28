with open("./Python-Home-Challenges/Challenge_01.txt") as file:
    fileArr = file.read().split()
    words = {}
    for word in fileArr:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    print(
        f'''Most recurring word in that file: {max(words, key=words.get)}
And it appears {words[max(words, key=words.get)]} times''')
