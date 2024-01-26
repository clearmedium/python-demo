def translate(text):
    words = text.split()
    processed_words = []

    for word in words:

        if word.isalpha() == False:
            return "You have entered an invalid character. Please enter a valid English word(s)."
        elif len(word) == 2 and word[1].lower() == 'y':
            processed_word = word[1] + word[0] +'ay'
        elif word[0].lower() in 'aeiou':
            processed_word = word + 'ay'
        elif word[0:2].lower() == 'xr' or word[0:2].lower == 'yt':
            processed_word = word + 'ay'
        elif word[0].lower() == 'y':
            processed_word = word[1:] + word[0] + 'ay'
        elif word[0] not in 'aeiouy' and word[1] in 'aeiou' and word[0:2] != 'qu':
            processed_word = word[1:] + word[0] + 'ay'
        elif word[0:2].lower() not in 'aeiouy' and word[1:3] != 'qu' and word[2] in 'aeiouy':
            processed_word = word[2:] + word[0:2] + 'ay'
        elif word[0:3].lower() not in 'aeiouy':
            processed_word = word[3:] + word[0:3] + 'ay'
        elif word[0] not in 'aeiouy' and word[1:3] == 'qu':
            processed_word = word[3:] + word[0:3] + 'ay'
        elif word[2] == 'y' and word[0:2] not in 'aeiouy':
            processed_word = word[2:] + word[0:2] + 'ay'
        else:
            processed_word = word
        processed_words.append(processed_word)

    return ' '.join(processed_words)



##Test Function
    
def test_translate():
    test_cases = [
        ("apple cat", "appleay atcay"),
    ]

    for text, expected in test_cases:
        result = translate(text)
        if result == expected:
            print(f"PASS: translate({text}) == {expected}")
        else:
            print(f"FAIL: translate({text}) -> {result} (expected: {expected})")

test_translate()

    # # Rule 1: If a word begins with a vowel sound, add an "ay" sound to the end of the word. Please note that "xr" and "yt" 
    # at the beginning of a word make vowel sounds (e.g. "xray" -> "xrayay", "yttria" -> "yttriaay").

    # # Rule 2: If a word begins with a consonant sound, move it to the end of the word and then add an "ay" sound to the end of the word. 
    # Consonant sounds can be made up of multiple consonants, such as the "ch" in "chair" or "st" in "stand" (e.g. "chair" -> "airchay").

    # # Rule 3: If a word starts with a consonant sound followed by "qu", move it to the end of the word, 
    # and then add an "ay" sound to the end of the word (e.g. "square" -> "aresquay").

    # # Rule 4: If a word contains a "y" after a consonant cluster or as the second letter in a two letter word it makes a 
    # vowel sound e.g. "rhythm" -> "ythmrhay", "my" -> "ymay"

