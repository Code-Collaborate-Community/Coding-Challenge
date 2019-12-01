
def most_frequent(List): 
    dict = {} 
    count, itm = 0, '' 
    for item in reversed(List): 
        dict[item] = dict.get(item, 0) + 1
        if dict[item] >= count : 
            count, itm = dict[item], item 
    return(itm) 

file = open('sample.txt','r')
data = file.read().replace('\n', '')
words = data.split()

print(f"The most occuring word is: {most_frequent(words)}")