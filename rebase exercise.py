def check_errors(input_base, digits, output_base):

    if input_base < 2:
        raise ValueError("input base must be >= 2")
    elif output_base < 2:
        raise ValueError("output base must be >= 2")
    
    for digit in digits:
        if digit < 0 or digit >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")


def convert_to_10(input_base, digits):
    base_10_result = 0

    for index, char in enumerate(digits):
        base_10_result += int(char) * input_base ** (len(digits) - (index + 1))
    
    return base_10_result

def rebase(input_base, digits, output_base):
    base_10_number = convert_to_10(input_base, digits)
    remainders = []

    while base_10_number != 0:
        remainders.append(base_10_number % output_base)
        base_10_number = base_10_number // output_base
    
    return remainders[::-1]


