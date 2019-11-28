
f = open("text.txt", "r")
if f.mode == 'r':
    contents = f.read().split()
    print(contents)

countDict={}

for word in contents:
    if word in countDict:
        countDict[word]=countDict[word]+1
    else:
        countDict[word] =1

max= max(countDict, key=countDict.get)
print("The word " +max + " is the most recurring word in that file")




f.close()