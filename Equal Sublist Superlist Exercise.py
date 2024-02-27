SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4

def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    elif is_sublist(list_one, list_two):
        return SUBLIST
    elif is_sublist(list_two, list_one):
        return SUPERLIST
    else:
        return UNEQUAL

def is_sublist(smaller, larger):
    """Check if smaller is a sublist of larger."""
    for i in range(len(larger) - len(smaller) + 1):
        if smaller == larger[i:i+len(smaller)]:
            return True
    return False