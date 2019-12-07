
def most_common_word(file_name):
    split_it = split_text(file_name)
    count_words_get_max(split_it)


def split_text(file_name):
    with open(file_name) as file:
        data_set = file.read()
        split_it = data_set.split()
        return split_it


def count_words_get_max(split_words):
    words_dict = {}
    for word in split_words:
        if word in words_dict.keys():
            words_dict[word] += 1
        else:
            words_dict.update({word: 1})
    maximum = max(words_dict, key=words_dict.get)
    print(maximum, words_dict[maximum])


if __name__ == "__main__":
    most_common_word("summary.txt")
