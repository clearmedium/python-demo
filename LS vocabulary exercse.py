##1

def add_prefix_un(word):
    unprefix = 'un'
    prefixapplied_word = unprefix + word

    return prefixapplied_word
    

##2

def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    combined_words = [prefix + word for word in vocab_words[1:]]

    return prefix + ' :: ' + ' :: '.join(combined_words)


##3

def remove_suffix_ness(word):
    suffix_removed_word = word[:-4]

    if suffix_removed_word.endswith('i'):
        return suffix_removed_word[:-1] + 'y'
    return suffix_removed_word


##4

def adjective_to_verb(sentence, index):
    words = sentence.split()
    verb = words[index].strip(',.')
    verbified_verb = verb + 'en'

    return verbified_verb