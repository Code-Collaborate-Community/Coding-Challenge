# HW03 - Open a text file and returns the most recurring word in that file.

with open(r'/home/$USER/', 'r') as fp:
    f = fp.readline()
# Read file #
split_words_from_file = f.split()

# Creating variable for checking what is the recurring value  #
biggest_counting = 0

for list_arg in split_words_from_file:
    count = 0
    for word in split_words_from_file:
        if list_arg == word:
            count += 1
    if count > biggest_counting:
        the_most_recurring_word = list_arg
        biggest_counting = count


print(f"The most recurring word in the file is '{the_most_recurring_word}'")
print(f"which has appeared {biggest_counting} times.")
