def convert_to_10(input_base, digits):
    base_10_result = 0

    for index, char in enumerate(digits):
        base_10_result += int(char) * input_base ** (len(digits) - (index + 1))
    
    return base_10_result

def rebase(input_base, digits, output_base):
    base_10_number = convert_to_10(input_base, digits)
    remainders = 0

    while base_10_number >= 1:
        base_10_number /= output_base
        remainders += base_10_number / output_base
        output_digits = ''.join([str(r) if r < 10 else chr(r - 10 + ord('A')) for r in reversed(remainders)])

    return output_digits













    
# The number 42, in base 10, means:

# (4 * 10^1) + (2 * 10^0)

# The number 101010, in base 2, means:

# (1 * 2^5) + (0 * 2^4) + (1 * 2^3) + (0 * 2^2) + (1 * 2^1) + (0 * 2^0)

# The number 1120, in base 3, means:

# (1 * 3^3) + (1 * 3^2) + (2 * 3^1) + (0 * 3^0)