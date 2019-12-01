text = open('text.txt', 'r') 
d = dict() 
for line in text: 
	 line = line.strip() 
	 line = line.lower() 
	 words = line.split(" ") 

	 for word in words: 
	 	if word in d:
	 		d[word] = d[word] + 1
	 	else: 
	 		d[word] = 1
for key in list(d.keys()): 
    print(key, ":", d[key]) 

mostapperdword=max(d,key=d.get)

print (mostapperdword)
print(max(d.values()))

print(f'The word that returns most times in the text file is: '  +mostapperdword+ ' and it returns ' ,max(d.values()))