# HW03 - Open a text file and returns the most recurring word in that file.

fp = open('/file.txt', 'r')
# Open file #
f = fp.readline()
# Read file #
split_words_from_file = f.split()

the_most_recurring_word = ''
biggest_counting = 0

copy_list = split_words_from_file
for list_arg in copy_list:
    for word in split_words_from_file:
        count = 0
        if list_arg == word:
            count += 1
    if count > biggest_counting:
        the_most_recurring_word = list_arg
        biggest_counting = count


print 'The word "{}" which has appeared {} times is the most recurring word in the file.'.format(the_most_recurring_word, biggest_counting)
fp.close()
# Close file #
