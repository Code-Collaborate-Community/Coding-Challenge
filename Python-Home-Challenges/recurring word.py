
where_file = input('Enter the file route: ')
my_file = open(where_file,"r")
print("Your file text is:")
for x in my_file:
  print(x)
print("---------------")
words_in_text = dict()
my_file = open(where_file,"r")
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
print (max(words_in_text.values()))

