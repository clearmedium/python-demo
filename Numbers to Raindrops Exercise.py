import operator

def convert(number):
    results = []

    if operator.mod(number, 3) == 0:
        results.append("Pling")
    if operator.mod(number, 5) == 0:
        results.append("Plang")
    if operator.mod(number, 7) == 0: 
        results.append("Plong")
    if operator.mod(number, 3) != 0 and operator.mod(number, 5) != 0 and operator.mod(number, 7) != 0:
        results.append(str(number))
    
    return ''.join(results)
#Code Testing
    
def convert_test():
    test_cases = [
        (15, "PlingPlang"),
    ]
    
    for number, expected in test_cases:
        result = convert(number)
        if result == expected:
            print(f"PASS: convert({number}) == {expected}")
        else: 
            print(f"FAIL: convert({number}) -> {result} (expected: {expected})")

convert_test()



# Your task is to convert a number into its corresponding raindrop sounds.

# If a given number:

#     is divisible by 3, add "Pling" to the result.
#     is divisible by 5, add "Plang" to the result.
#     is divisible by 7, add "Plong" to the result.
#     is not divisible by 3, 5, or 7, the result should be the number as a string.

# Examples

#     28 is divisible by 7, but not 3 or 5, so the result would be "Plong".
#     30 is divisible by 3 and 5, but not 7, so the result would be "PlingPlang".
#     34 is not divisible by 3, 5, or 7, so the result would be "34".
# operator.mod(a, b)