#  Refactor homeworks from module 2 and 3 using functional approach with decomposition.

# Ensure that functions have proper docstrings, type hints and return annotation.

import random
import string
from typing import List, Dict
from pprint import pprint


def generate_dict_list(number_of_dictionaries: int) -> List[Dict[str, int]]:
    """
    Generate randomized list of dictionaries ranging from 2 to given input.
    Number of keys is randomized from 2 to 10, and uses set of random letters from A to O.
    Values are based on random number from 0 to 100

    :param number_of_dictionaries: Maximum number of dictionaries to generate (must be >= 2 as 2 is min).
    :return: List[Dict[str, int]]: A list of randomly generated dictionaries with letters as key and number as value.
    """

    if number_of_dictionaries < 2:
        raise ValueError('number_of_dictionaries must be greater than 2')

    dict_list = [
        {
            key: random.randint(0, 100)
            for key in random.sample(string.ascii_lowercase[:15], random.randint(2, 10))
        }

        for _ in range(random.randint(2, number_of_dictionaries))

    ]

    return dict_list


def generate_inverted_index(list_to_invert: List[Dict[str, int]]) -> Dict[str, List[List[int]]]:
    """
    Creates inverted index based on list of dictionaries.
    Uses all unique keys found across all dictionaries and uses dictionary id + value as values to mark where can that key be found in original list of dictionaries.
    Enumerate is used to assign dict_id based on index, starting from 1.

    :param list_to_invert: List of dictionaries with str, int pairs i.e. [{'a': 10, 'b':15}, {'a':5, 'c':29}].
    :return: Dictionary with all keys from original list and values highlighting in which dictionary (id based on position in original list) can the key be found, and what value was assigned.
    """

    keys_set = {key for d in list_to_invert for key in d.keys()}

    inverted_keys_dict = {k: [] for k in keys_set}

    for dict_id, single_dict in enumerate(list_to_invert, start=1):
        for key in single_dict:
            inverted_keys_dict[key].append([dict_id, single_dict[key]])

    return inverted_keys_dict


def create_final_dictionary(inverted_index_dict: Dict[str, List[List[int]]]) -> Dict[str, int]:
    """
    Creates dictionary with list of all keys from original dictionaries and their highest value.

    Formats key based on below requirements:
    - If key appeared only once, leave as it is i.e. 'a': 59.
    - If key appeared multiple times, add "_" and number for dictionary with the highest value for that key i.e. 'a_5': 59.

    :param inverted_index_dict: Dictionary containing keys and list of all directories in which key can be found with its value in that dictionary.
    :return: Dictionary with formatted keys and maximum value for said key across all original directories.
    """

    final_dict = {}

    for key, entries in inverted_index_dict.items():
        if len(entries) == 1:
            final_dict[key] = entries[0][1]

        else:
            final_key = f'{key}_{entries[0][0]}'
            final_value = entries[0][1]
            for inner_list in entries:
                if inner_list[1] > final_value:
                    final_key = f'{key}_{inner_list[0]}'
                    final_value = inner_list[1]

            final_dict[final_key] = final_value

    final_sorted_dict = dict(sorted(final_dict.items()))

    return final_sorted_dict


if __name__ == '__main__':

    dict_list = generate_dict_list(12)
    generate_inverted_index = generate_inverted_index(dict_list)
    final_dict = create_final_dictionary(generate_inverted_index)

    pprint(final_dict)
