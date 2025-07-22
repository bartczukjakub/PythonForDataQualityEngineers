# Refactor homeworks from module 2 and 3 using functional approach with decomposition.

# Ensure that functions have proper docstrings, type hints and return annotation.

def remove_non_ascii_string(text_input: str) -> str:
    """
    Breaks down input string, removes non-ASCII characters except “ and ” special double quotes, joins characters back.

    :param text_input: Text in string format.
    :return: Text in the same format without non-ASCII characters.
    """

    text_without_non_ascii = [letter for letter in text_input if letter.isascii() or letter in ('“', '”')]
    string_without_non_ascii = ''.join(text_without_non_ascii).strip()

    return string_without_non_ascii


def trim_and_capitalize_text(input_text: str) -> str:
    """
    Splits the text into lines using dot as delimiter, strips any leading or following spaces, or additional linebreaks, capitalizes each sentence.

    :param input_text: Text in string format.
    :return: Text without any leading or following spaces, or additional linebreaks, with capitalized sentences.
    """

    text_split_to_lines = input_text.replace('\n', '').replace('.', '.\n').splitlines()
    formatted_lines = [sentence.strip().capitalize() for sentence in text_split_to_lines]
    cleaned_text = ' '.join(formatted_lines)

    return cleaned_text


def replace_string(input_string: str, str_replace_from: str, str_replace_to: str) -> str:
    """
    Replaces old string with new one and returns text in the same format.

    :param input_string: Structured text with dots between sentences.
    :param str_replace_from: String that will be replaced.
    :param str_replace_to: String that will be used instead.
    :return: Text with replaced strings.
    """

    new_text_list = []

    for line in input_string.splitlines():
        for word in line.split(' '):
            if word == str_replace_from:
                new_text_list.append(str_replace_to)
            else:
                new_text_list.append(word)

    return ' '.join(new_text_list)


def create_sentence_from_last_word_in_each_sentence(text_split_to_lines: str) -> str:
    """
    Creates a new sentence based on last word in each sentence.

    :param text_split_to_lines: Structured text with dots between sentences.
    :return: Input text with additional sentence in the same format.
    """

    new_sentence = ' '.join([sentence.split(' ')[-1] for sentence in text_split_to_lines.strip().split('. ')]).capitalize()
    return text_split_to_lines + ' ' + new_sentence


def count_whitespaces(input_text: str) -> str:
    """
    Counts number of whitespaces used in text utilizing char.isspace() method.

    :param input_text: Text from which whitespaces will be count.
    :return: Text with count of whitespaces.
    """

    return f'Total number of whitespaces in the text = {sum(1 for char in input_text if char.isspace())}.'


if __name__ == '__main__':

    with open('./input_string', 'r', encoding='utf8') as file:
        file_body = file.read()

        print(create_sentence_from_last_word_in_each_sentence(
                replace_string(
                    trim_and_capitalize_text(
                        remove_non_ascii_string(file_body)
                    ),
                'iz', 'is')
                )
            )

    # Counter

        print(count_whitespaces(file_body))