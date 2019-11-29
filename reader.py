def main():
    while True:
        try:
            path = path_input()
            if path:
                file = open_file(path)
            else:
                file = open_file()
            break
        except FileNotFoundError as e:
            print(f'File not found! \n{e}\nTry again:')
    top_word, word_appear = max_frequency(fetch_words(file))
    file.close()
    print(f'Most frequent word is "{top_word}", '
          f'and it appears {word_appear} times.')


def path_input():
    answer = input("Insert the file's full path "
                   "OR press Enter to use the default path:")
    if answer is None:
        return
    return answer


def max_frequency(words):
    most_frequent = max(words, key=words.get)
    return most_frequent, words[most_frequent]


def fetch_words(file):
    words = dict()
    for line in file:
        for word in line.strip("!@#$%^&*()_-+=~`,.':;<>\n").split(' '):
            if word != '':
                words[word.lower()] = words.get(word, 0) + 1
    return words


def open_file(path='./Python-Home-Challenges/Challenge_01.txt'):
    return open(path, 'r')


if __name__ == '__main__':
    main()
