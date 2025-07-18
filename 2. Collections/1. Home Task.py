# Write a code, which will:

# 1. create a list of random number of dicts (from 2 to 10)

# dict's random numbers of keys should be letter,
# dict's values should be a number (0-100),
# example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]

# 2. get previously generated list of dicts and create one common dict:

# if dicts have same key, we will take max value, and rename key with dict number with max value
# if key is only in one dict - take it as is,
# example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}
# Each line of code should be commented with description.

import random
import string
from pprint import pprint

# 1. Create a list of random number of dicts (from 2 to 10), with letters as keys and numbers as values.

dict_list = []

# Loop to create from 2 to 10 dictionaries

for i in range(random.randint(2,10)):
    dict_sample = {}

    # Loop to create from 2 to 10 randomized keys

    for i in range(random.randint(2,10)):

        # Random letter will be assigned as a key. Reducing number of letters to A - O to increase keys overlap within dictionaries.

        dict_key = random.choice(string.ascii_lowercase[:15])

        # Checks if the letter was already used

        while dict_key in dict_sample.keys():
            dict_key = random.choice(string.ascii_lowercase[:10])

        # Assigns random value as integer from 0 to 100 to a key

        dict_value = random.randint(0,100)
        dict_sample[dict_key] = dict_value

    # Appends dictionary to main list

    dict_list.append(dict_sample)


# 2. get previously generated list of dicts and create one common dict:

# Inverted Index is the answer?
# The idea is to create a dictionary with all unique keys from dictionaries within original list, with information in which dictionary form the original list did the key appear, and what was it's value.

# Create empty list and populate it with all keys from every single dictionary

keys_list = []

for single_dict in dict_list:
    keys_list += (key for key in single_dict.keys())

# Create set based on sorted list to remove duplicate and make future dictionary cleaner

keys_set = set(sorted(keys_list))

# Create dictionary with empty lists based on all keys from set

inverted_keys_dict = {k: [] for k in keys_set}

# Loop through all keys and then through all dictionaries in the initially created list.

for key in inverted_keys_dict.keys():
    for single_dict in dict_list:

        # Creating dictionary id based on it's index within original list

        dict_id = dict_list.index(single_dict) + 1

        # Looping through separate dictionaries from original list to validate if keys within this dictionary match with keys from inverted index dictionary (inverted_keys_dict).
        # If so, add dict_id and value to the inverted index.

        for k, v in single_dict.items():
            if k == key:
                inverted_keys_dict[key].append([dict_id, v])

# Once again, the end result of the above loop is dictionary with all unique keys from dictionaries within original list, with information in which dictionary form the original list did the key appear, and what was it's value.
# Printing dict to see the collection

pprint(inverted_keys_dict)

final_dict = {}

# Now we loop through values for each key.
# If key has only one value then the key remains the same, and it's value is pulled from first item in the list.

for key, value in inverted_keys_dict.items():
    if len(value) == 1:
        final_value = value[0][1]
        final_dict[key] = final_value

    # If length of the value list is greater than 1 then we create "final" key and value based on first item within the list, with appropriate format. Addint +1 to the index value to match criteria.
    # Next we loop through all other lists to validate if there's another list (original dictionary) with greater value than the first one. If so, this pair becomes the "final" key value pair

    else:
        final_key = f'{key}_{value[0][0]+1}'
        final_value = value[0][1]
        for inner_list in value:
            if inner_list[1] > final_value:
                final_key = f'{key}_{inner_list[0]+1}'
                final_value = inner_list[1]

        # Once the inner loop finishes, the final final key value pair is added to the final dictionary

        final_dict[final_key] = final_value

# Sorting dictionary

final_sorted_dict = dict(sorted(final_dict.items()))

print(final_sorted_dict)
