text_to_fix = """  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

# Removing non-ascii characters

text_without_non_ascii = [letter for letter in text_to_fix if letter.isascii() or letter in ('“', '”')]

# Merging letters together. Yes this step can be combined with the above, this just looks cleaner and simpler to me.

string_without_non_ascii = ''.join(text_without_non_ascii).strip()

# Splitting string into proper text lines.

text_split_to_lines = string_without_non_ascii.replace('\n', '').replace('.', '.\n').splitlines()

# Converting "iz" to "is"

new_text_list = []

for line in text_split_to_lines:
    for word in line.strip().capitalize().split(' '):
        if word == 'iz':
            new_text_list.append('is')
        else:
            new_text_list.append(word)

# Creating clean string

cleaned_text = ' '.join(new_text_list)

# Creating sentence from last words. Is this comprehension even readable?

new_sentence_unreadable_comprehension = ' '.join([line.strip().capitalize().replace('.', '').split(' ')[-1] for line in text_split_to_lines]).capitalize() + '.'

# Adding new sentence to cleaned text

cleaned_text_with_new_sentence = ' '.join(new_text_list) + ' ' + new_sentence_unreadable_comprehension

print(cleaned_text_with_new_sentence)

# Whitespaces counter. Doing it via dict to actually see what characters do I have

char_dict = {}

for char in text_to_fix:
    if not char.isalnum() and char not in (',', '“', '”', '.'):
        char_dict[char] = char_dict.get(char, 0) + 1

print(char_dict)

# No matter the combination I can't get the number 87 :| I guess it might be related with what part of the text is copied?

sum_of_chars = sum(char_dict.values())

print(sum_of_chars)
