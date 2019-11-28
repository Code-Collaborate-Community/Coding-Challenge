file_object =open("a.txt","r")
data=file_object.read().split()
dict = {}
for i in data:
    if i in dict:
        dict[i] =  dict[i] + 1
    else:
        dict[i] = 1
print(f'the word that appears most is: {max(dict, key=dict.get)}, And it appears {dict[max(dict, key=dict.get)]} times')