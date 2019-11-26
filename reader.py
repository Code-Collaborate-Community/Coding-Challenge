def main():
    find_word_frequency()


def max_frequency(words):
    most_frequent = max(words, key=words.get)
    print(most_frequent, words[most_frequent])


def find_word_frequency():
    try:
        with open('./Python-Home-Challenges/Challenge_01.txt', 'r') as file:
            words = dict()
            for line in file:
                for word in line.strip(",.!:\n").split(' '):
                    if word is not '':
                        words[word.lower()] = words.get(word, 0) + 1
            return max_frequency(words)
    except FileNotFoundError as e:
        print('File not found')

if __name__ == '__main__':
    main()
