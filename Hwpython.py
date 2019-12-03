#my code:

with open('text.txt') as file:
    List=file.read().split()
    wordDict={}
    for word in List:
           if word in wordDict:
               wordDict[word]+=1
           else:
                wordDict[word]=1

    print(f' the most recurring word in that file: {max(wordDict, key=wordDict.get)}')
    print(f'Appears {wordDict[max(wordDict,key=wordDict.get)]} times')



