def classify(number):
    division_list = []

    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    # 1 is a special case when dealing with aliquot sum and perfect numbers.
    if number == 1:
        return "deficient"
    
    for i in range(1, number//2 + 1):
        if number % i == 0:
            division_list.append(i)

    for char in division_list:
        if sum(division_list) == number:
            return "perfect"
        elif sum(division_list) > number: 
            return "abundant"
        elif sum(division_list) < number:
            return "deficient"
        

def test_classify():
    test_cases = [
        (1,"deficient"),
    ]

    for number , expected in test_cases:
        result = classify(number)
        if result == expected: 
            print(f"PASS: classify({number}) == ({expected})")
        else: 
            print(f"FAIL: classify({number}) -> {result} (expected:{expected})")

test_classify()