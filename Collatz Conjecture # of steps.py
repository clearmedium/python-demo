def steps(number):
    if number <= 0: 
        #Returns an error if the number entered is less than zero
        raise ValueError("The number is negative.")
    elif not isinstance(number, int): 
        #Returns an error if the number entered is not a whole number. 
        raise ValueError("The number is not a whole integer.") 
        
    steps = 0

    while number > 1:
        if number % 2 == 0:
            number = number // 2 
        else:
            number = number * 3 + 1
        steps += 1
    print(steps)
    return steps
# Example call to the function
steps(0)


    #This returns the number of steps it will take to get to 1 using the Collatz Conjecture



#Collatz Conjecture for reference is: Take any positive integer n. If n is even, divide n by 2 to get n / 2. If n is odd, multiply n by 3 and add 1 to get 3n + 1. 


# # Reference example on how to solve this recursively instead: 

# def steps(number):
#     if number <= 0:
#         raise ValueError("Only positive integers are allowed")
#     if number == 1:
#         return 0
#     number = number / 2 if number % 2 == 0 else number * 3 + 1
#     return 1 + steps(number)