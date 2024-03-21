def is_paired(input_string):
    bracketsr = []
    bracesr = []
    parensr = []
#THIS IS ON THE RIGHT TRACK: fix the fact that it does not account for nested pairs and instead look for a way to do comparison by iterating through the string with all the non {}[]() characters removed. 
    for char in input_string:
        if char == "[" or char == "]":
            bracketsr.append(char)
        if char == "{" or char == "}":
            bracesr.append(char)
        if char == "(" or char == ")":
            parensr.append(char)
        else:
            continue
    
    if all(item == "[" for item in bracketsr[0::2]) and all(item == "]" for item in bracketsr[1::2]) and all(item == "{" for item in bracesr[0::2]) and all(item == "}" for item in bracesr[1::2]) and all(item == "(" for item in parensr[0::2]) and all(item == ")" for item in parensr[1::2]):
        return True
    else: 
        return False
        

    






# Given a string containing brackets [], braces {}, parentheses (), or any combination thereof, verify that any and all pairs are matched and nested correctly. The string may also contain other characters, which for the purposes of this exercise should be ignored.

# ex: ("{)()"), False
# ("([{}({}[])])"), True