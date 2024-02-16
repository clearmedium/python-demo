import string

def is_pangram(sentence):
    sentence_low = sentence.lower()
    letter_count = {}
    
    for char in sentence_low:
        if char in string.ascii_lowercase:
            letter_count[char] = letter_count.get(char, 0) + 1
        else: letter_count[char] = 0
    
    for char in string.ascii_lowercase:
        if letter_count.get(char, 0) < 1:
            return False
    return True
        

def test_panagram():
    test_cases = [
        ("7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog", False )
    ]

    for sentence, expected in test_cases:
        result = is_pangram(sentence)
        if result == expected:
            print(f"PASS: is_panagram({sentence}) == {expected}")
        else: 
            print(f"FAIL: is_panagram({sentence}) -> {result} (expected: {expected})")

test_panagram()





# Instructions

# Your task is to figure out if a sentence is a pangram.

# A pangram is a sentence using every letter of the alphabet at least once. It is case insensitive, so it doesn't matter if a letter is lower-case (e.g. k) or upper-case (e.g. K).

# For this exercise, a sentence is a pangram if it contains each of the 26 letters in the English alphabet.
