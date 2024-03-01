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
    check_errors(input_base, digits, output_base)

    base_10_number = convert_to_10(input_base, digits)
    remainders = []

    if not digits:
        return [0]

    while base_10_number != 0:
        remainders.append(base_10_number % output_base)
        base_10_number = base_10_number // output_base

    if not remainders:
        return [0]
    
    return remainders[::-1]


def test_rebase():
    test_cases = [
            (1, [0], 10, ValueError),
    ]

    for input_base, digits, output_base, expected in test_cases:
        result = rebase(input_base, digits, output_base)
        if result == expected:
            print(f"PASS: rebase({input_base}, {digits}, {output_base}) == {expected}")
        else: print(f"FAIL: rebase({input_base}, {digits}, {output_base}) -> {result} (expected: {expected})")

test_rebase()