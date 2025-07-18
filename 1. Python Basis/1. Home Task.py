# What should be done

# Create list of 100 random numbers from 0 to 1000
# Sort list from min to max (without using sort())
# Calculate average for even and odd numbers
# Print both average result in console
# Each line of code should be commented with description

import random

# 1. Create list of 100 random numbers from 0 to 1000

# Create empty list

number_list = []

# Generate random 100 numbers fron range of 0-1000 and append them to number_list

for num in range(100):
    number_list.append(random.randint(0,1000))

# 2. Sort list from min to max (without using sort())

# Create new list for sorted values

sorted_list = []

#  Do the loop X times, equal to length of original list, and with each loop append minimum value from original list to the sorted list.
#  In each loop this minimum value is being removed from original list so the next loop selects another min value.

for num in range(len(number_list)):
    num_to_append = min(number_list)
    sorted_list.append(num_to_append)
    number_list.remove(num_to_append)

# 3. Calculate average for even and odd numbers

# Create lists with even and odd numbers

even_list = [number for number in sorted_list if number % 2 == 0]
odd_list = [number for number in sorted_list if number not in even_list]

# Calculate averages for numbers in even and odd lists

even_number_average = round(sum(even_list) / len(even_list), 2)
odd_list_average = round(sum(odd_list) / len(odd_list), 2)

# 4. Print both average results in console

print(even_number_average, odd_list_average)
