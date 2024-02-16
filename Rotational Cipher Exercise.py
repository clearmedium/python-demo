import string

def rotate(text, key):
    max_value = 26
    conversion_results = []
    
    for char in text:
        if char in string.ascii_lowercase:
            conversion_lower = (string.ascii_lowercase.find(char) + key) % max_value
            conversion_results.append(string.ascii_lowercase[conversion_lower])
        elif char in string.ascii_uppercase:
            conversion_upper = (string.ascii_uppercase.find(char)+ key) % max_value
            conversion_results.append(string.ascii_uppercase[conversion_upper])
        else:
            conversion_results.append(char)

    return ''.join(conversion_results)

def test_rotate():
    test_cases = [
        ("NM", 13,"AZ"),
    ]

    for text, key, expected in test_cases:
        result = rotate(text, key)
        if result == expected:
            print(f"PASS: rotate({text}, {key}) == {expected}")
        else:
            print(f"FAIL: rotate({text}, {key}) -> {result} (expected: {expected})")

test_rotate()






# Create an implementation of the rotational cipher, also sometimes called the Caesar cipher.

# The Caesar cipher is a simple shift cipher that relies on transposing all the letters in the alphabet using an integer key between 0 and 26. Using a key of 0 or 26 will always yield the same output due to modular arithmetic. The letter is shifted for as many values as the value of the key.

# The general notation for rotational ciphers is ROT + <key>. The most commonly used rotational cipher is ROT13.

# A ROT13 on the Latin alphabet would be as follows:
         #1  
# Plain:  abcdefghijklmnopqrstuvwxyz
# Cipher: nopqrstuvwxyzabcdefghijklm

# It is stronger than the Atbash cipher because it has 27 possible keys, and 25 usable keys.

# Ciphertext is written out in the same formatting as the input including spaces and punctuation.
# Examples

#     ROT5 omg gives trl
#     ROT0 c gives c
#     ROT26 Cool gives Cool
#     ROT13 The quick brown fox jumps over the lazy dog. gives Gur dhvpx oebja sbk whzcf bire gur ynml qbt.
#     ROT13 Gur dhvpx oebja sbk whzcf bire gur ynml qbt. gives The quick brown fox jumps over the lazy dog.

