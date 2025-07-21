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
# Creates key based on list of 2-10 random letters from a - o
# Creates value based on random number from 0 - 100

dict_list = [
    {
        key: random.randint(0,100)
        for key in random.sample(string.ascii_lowercase[:15], random.randint(2,10))
    }

    for _ in range(random.randint(2,10))

]

# 2. get previously generated list of dicts and create one common dict:

# Inverted Index is the answer?
# The idea is to create a dictionary with all unique keys from dictionaries within original list, with information in which dictionary (form the original list) did the key appear, and what was its value.

# Create set and populate it with all keys from every single dictionary

keys_list = {key for d in dict_list for key in d.keys()}

# Create dictionary with empty lists based on all keys from set

inverted_keys_dict = {k: [] for k in keys_list}

# Loop through all separate dictionaries in original dict_list via enumerate to also get index id. Adding start to match formatting criteria for final dictionary keys.

for dict_id, single_dict in enumerate(dict_list, start = 1):

    # Adding key value pairs from separate dictionaries into inverted index

    for key in single_dict:
        inverted_keys_dict[key].append([dict_id, single_dict[key]])

# Once again, the end result of the above loop is dictionary with all unique keys from dictionaries within original list, with information in which dictionary form the original list did the key appear, and what was it's value.
# Printing dict to see the collection

pprint(inverted_keys_dict)

final_dict = {}

# Now we loop through values for each key.
# If key has only one value then the key remains the same, and it's value is pulled from first item in the list.

for key, entries in inverted_keys_dict.items():
    if len(entries) == 1:
        final_dict[key] = entries[0][1]

    # If length of the value list is greater than 1 then we create "final" key and value based on first item within the list, with appropriate format. Addint +1 to the index value to match criteria.
    # Next we loop through all other lists to validate if there's another list (original dictionary) with greater value than the first one. If so, this pair becomes the "final" key value pair

    else:
        final_key = f'{key}_{entries[0][0]}'
        final_value = entries[0][1]
        for inner_list in entries:
            if inner_list[1] > final_value:
                final_key = f'{key}_{inner_list[0]}'
                final_value = inner_list[1]

        # Once the inner loop finishes, the final final key value pair is added to the final dictionary

        final_dict[final_key] = final_value

# Sorting dictionary

final_sorted_dict = dict(sorted(final_dict.items()))

print(final_sorted_dict)
