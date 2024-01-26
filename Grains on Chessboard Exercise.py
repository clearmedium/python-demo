def square(number):

    if number < 1 or number > 64 or number != int(number):
        raise ValueError("square must be between 1 and 64")
    return pow(2, number -1)


def total():
    total_sum = 0
    
    for number in range(1, 65):
        total_sum += pow(2, number - 1)
    return total_sum














# # when the square value is not in the acceptable range        
# raise ValueError("square must be between 1 and 64")