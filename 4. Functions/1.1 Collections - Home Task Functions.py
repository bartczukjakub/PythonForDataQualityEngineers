#  Refactor homeworks from module 2 and 3 using functional approach with decomposition.

# Ensure that functions have proper docstrings, type hints and return annotation.

import random
import string
from typing import List, Dict
from pprint import pprint


def dict_list_generator(number_of_dictionaries: int) -> List[Dict[str, int]]:
    """
    Generate randomized list of dictionaries ranging from 2 to given input.

    :param number_of_dictionaries: Maximum number of dictionaries to generate (must be >= 2 as 2 is min).
    :return: List[Dict[str, int]]: A list of randomly generated dictionaries with letters as key and number as value.
    """

    # Checks if input < 2 and if so raises an Error

    if number_of_dictionaries < 2:
        raise ValueError('number_of_dictionaries must be greater than 2')

    # Loop to create from 2 to X dictionaries specified by function arguments
    # Creates key based on list of 2-10 random letters from a to o
    # Creates value based on random number from 0 to 100.

    dict_list = [
        {
            key: random.randint(0, 100)
            for key in random.sample(string.ascii_lowercase[:15], random.randint(2, 10))
        }

        for _ in range(random.randint(2, number_of_dictionaries))

    ]

    return dict_list


def inverted_index_generator(list_to_invert: List[Dict[str, int]]) -> Dict[str, List[List[int]]]:
    """
    Creates inverted index based on list of dictionaries.

    :param list_to_invert: List of dictionaries with str, int pairs i.e. [{'a': 10, 'b':15}, {'a':5, 'c':29}].
    :return: Dictionary with all keys from original list and values highlighting in which dictionary (id based on position in original list) can the key be found, and what value was assigned.
    """

    # Create a set and populate it with all unique keys from dictionaries

    keys_set = {key for d in list_to_invert for key in d.keys()}

    # Create dictionary with empty lists based on all keys from set

    inverted_keys_dict = {k: [] for k in keys_set}

    # Loops through input list of dictionaries, use enumerate to assign dict_id based on index (starting from 1)
    # Adds dict_id + value as values for a corresponding key in inverted index dictionary.

    for dict_id, single_dict in enumerate(list_to_invert, start=1):
        for key in single_dict:
            inverted_keys_dict[key].append([dict_id, single_dict[key]])

    return inverted_keys_dict


def create_final_dictionary(inverted_index_dict: Dict[str, List[List[int]]]) -> Dict[str, int]:
    """
    Formats key based on below requirements:
    - If key appeared only once, leave as it is i.e. 'a': 59.
    - If key appeared multiple times, add "_" and number for dictionary with the highest value for that key i.e. 'a_5': 59.

    Assigns highest value for key found across all original dictionaries.

    :param inverted_index_dict: Dictionary containing keys and list of all directories in which key can be found with its value in that dictionary.
    :return: Dictionary with formatted keys and maximum value for said key across all original directories.
    """

    final_dict = {}

    # If length of the value list is greater than 1 then we create "final" key and value based on first item within the list, with appropriate format.

    for key, entries in inverted_index_dict.items():
        if len(entries) == 1:
            final_dict[key] = entries[0][1]

        # Next we loop through all other lists to validate if there's another list (original dictionary) with greater value than the first one. If so, this pair becomes the "final" key value pair.

        else:
            final_key = f'{key}_{entries[0][0]}'
            final_value = entries[0][1]
            for inner_list in entries:
                if inner_list[1] > final_value:
                    final_key = f'{key}_{inner_list[0]}'
                    final_value = inner_list[1]

            # Once the inner loop finishes, the "final final" key value pair is added to the final dictionary.

            final_dict[final_key] = final_value

    # Sorting dictionary

    final_sorted_dict = dict(sorted(final_dict.items()))

    return final_sorted_dict


if __name__ == '__main__':
    result = (create_final_dictionary(inverted_index_generator(dict_list_generator(12))))
    pprint(result)
