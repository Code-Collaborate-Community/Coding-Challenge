
where_file = input('Enter the file route: ')
with open(where_file,"r") as file:
    my_file =file.readlines()
words_in_text = dict()
for line in my_file:
    line = line.strip()
    words = line.split(" ")
    for word in words:
        if word in words_in_text:
            words_in_text[word] = words_in_text[word] + 1
        else:
            words_in_text[word] = 1
for key in list(words_in_text.keys()):
    print(key, ":", words_in_text[key])
print("---------------")
max1=0
for highest in list(words_in_text.keys()):
    if max1 < words_in_text[highest]:
        max1 = words_in_text[highest]
        key1 = highest
print (("The most recurring word is: {key12} with {max12} times").format(key12=key1,max12=max1))
