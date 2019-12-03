#my code:

with open('text.txt', 'r') as file:
    f_read=file.read().split()
    word_counter={}
    for word in List:
           if word in wordDict:
               word_counter[word]+=1
           else:
                word_counter[word]=1

    print(f' the most recurring word in that file: {max(wordDict, key=wordDict.get)}')
    print(f'Appears {wordDict[max(wordDict,key=wordDict.get)]} times')



