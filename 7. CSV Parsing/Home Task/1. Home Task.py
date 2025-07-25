import csv
from collections import Counter

def count_all_words() -> None:
    """
    Counts words from input file, counts their occurrences and saves CSV with this data.

    :return: Csv file with each word and its count in text.
    """
    with open('./Files to process/input.txt', 'r', encoding= 'utf8') as file:
        file_content = file.read()

    words_dict = {}

    for word in file_content.lower().replace('.', '').replace(',', '').split(' '):
        words_dict[word] = words_dict.get(word, 0) + 1

    with open('./words_count.csv', 'w', encoding= 'utf8') as file:

        for key, value in sorted(words_dict.items()):
            record = f'{key.strip()},{value}\n'
            file.write(record)


def count_words_with_stats() -> None:
    """
    Counts words from input file, counts words occurrences, count of occurrences if word was also Title format, and percentage of word usage.
    Saves csv file with this data.
    Utilizes Counter from collections.

    :return: CSV file with each word, required occurrences and percentage of usage.
    """

    with open('./Files to process/input.txt', 'r', encoding= 'utf8') as file:
        file_content = file.read()

    raw_words = [word for word in file_content.lower().replace('.', '').replace(',', '').split(' ')]

    total_words = len(raw_words)

    lower_words = Counter(word.lower() for word in raw_words)

    title_words = Counter(word.lower() for word in raw_words if word.istitle())

    words_dict = {
        word: {
            'all': count,
            'upper': title_words.get(word,0),
            'percentage': count / total_words
        }
        for word, count in lower_words.items()
    }

    with open('./words_count_with_stats.csv', 'w', encoding= 'utf8', newline= '') as output:
        writer = csv.writer(output)
        writer.writerow(['letter', 'count_all', 'count_uppercase', 'percentage'])

        for key, value in sorted(words_dict.items()):
            writer.writerow([key, value['all'], value['upper'], value['percentage']])


if __name__ == '__main__':
    count_all_words()
    count_words_with_stats()
