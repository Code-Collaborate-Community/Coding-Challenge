# HW03 - Open a text file and returns the most recurring word in that file.


def read_file():
    with open('../file.txt', 'r') as tmp_file:
        execute_file = tmp_file.readline()
    return execute_file


def spilt_file(file):
    split_words_from_file = file.split()
    return split_words_from_file


def printing_the_recurring_word(split_words_from_file):
    biggest_counting = 0
# Creating variable for keeping the recurring value from the file #
    words = dict()
    for list_arg in split_words_from_file:
        if list_arg in words:
            words[list_arg] = words[list_arg] + 1
    else:
        words[list_arg] = 1

    for key in words:
        if words[key] > biggest_counting:
            biggest_counting = words[key]
            the_most_recurring_word = key
    print(f"The most recurring word: '{the_most_recurring_word}'")
    print(f"which has appeared {biggest_counting} times.")


def main():
    my_file = read_file()
    my_split_file = spilt_file(my_file)
    printing_the_recurring_word(my_split_file)


main()
