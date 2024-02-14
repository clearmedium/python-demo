import string

def is_isogram(input_string):
    alphabet = string.ascii_lowercase
    string_lower = input_string.lower()
    letter_count = {}

    for char in string_lower:

        if char in alphabet:
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1
    
    if all(count == 1 for count in letter_count.values()):
        return True
    else:
        return False






# Determine if a word or phrase is an isogram.

# An isogram (also known as a "non-pattern word") is a word or phrase without a repeating letter, however spaces and hyphens are allowed to appear multiple times.

# Examples of isograms:

#     lumberjacks
#     background
#     downstream
#     six-year-old

# The word isograms, however, is not an isogram, because the s repeats.
