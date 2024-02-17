import string

def is_valid(isbn):
    filtered_chars = ([char for char in isbn if char.isalnum()])
    r = []

    for char in filtered_chars:
        if char in string.ascii_letters and char.lower() != 'x':
            return False
        elif char.isdigit():
            r.append(int(char))
        else: 
            continue

    if len(filtered_chars) != 10:
        return False
    elif filtered_chars[9].lower() == 'x':
        isbn_maths = (r[0] * 10 + r[1] * 9 + r[2] * 8 + r[3] * 7 + r[4] * 6 + r[5] * 5 + r[6] * 4 + r[7] * 3 + r[8] * 2 + 10 * 1) % 11 == 0
    elif len(r) != 10:
        return False
    else:
        isbn_maths = (r[0] * 10 + r[1] * 9 + r[2] * 8 + r[3] * 7 + r[4] * 6 + r[5] * 5 + r[6] * 4 + r[7] * 3 + r[8] * 2 + r[9] * 1) % 11 == 0
    
    return isbn_maths

def test_is_valid():
    test_cases = [
        ("359821507", False)
    ]

    for isbn, expected in test_cases:
        result = is_valid(isbn)
        if result == expected:
            print(f"PASS: is_valid({isbn}) == {expected}")
        else:
            print(f"FAIL: is_valid({isbn}) -> {result} (expected: {expected})")

test_is_valid()
    







# ISBN

# The ISBN-10 format is 9 digits (0 to 9) plus one check character (either a digit or an X only). In the case the check character is an X, this represents the value '10'. These may be communicated with or without hyphens, and can be checked for their validity by the following formula:

# Formula:
# (d₁ * 10 + d₂ * 9 + d₃ * 8 + d₄ * 7 + d₅ * 6 + d₆ * 5 + d₇ * 4 + d₈ * 3 + d₉ * 2 + d₁₀ * 1) mod 11 == 0

# Task

# Given a string the program should check if the provided string is a valid ISBN-10. Putting this into place requires some thinking about preprocessing/parsing of the string prior to calculating the check digit for the ISBN.

# The program should be able to verify ISBN-10 both with and without separating dashes.
# Caveats

# Converting from strings to numbers can be tricky in certain languages. Now, it's even trickier since the check digit of an ISBN-10 may be 'X' (representing '10'). For instance 3-598-21507-X is a valid ISBN-10.