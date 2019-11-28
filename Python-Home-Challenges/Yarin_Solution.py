
def most_common_word(file_name):
    words_dict={}
    with open(file_name) as file:
        data_set=file.read()
        split_it= data_set.split()
        for word in split_it:
            if word in words_dict.keys():
                words_dict[word]+=1
            else:
                words_dict.update({word:1})
        maximum = max(words_dict, key=words_dict.get)
        print(maximum, words_dict[maximum])



if __name__== "__main__":
    file_name = input("insert file path: ")
    most_common_word(file_name)


