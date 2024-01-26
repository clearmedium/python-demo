# round((1.20*float(10/100))+1.20, 2) #first part of the exercise that gets the 1.32 result needed for conversion rate + spread figured in. 

# 127.25/round((1.20*float(10/100))+1.20, 2)//5*5 
#this is the full exercise currenct calculator result. this takes the budget/round((exchange_rate*float(spread/100))+exchange_rate,2)//denomination*denomination
#this version is correct but I am saving this as a reminder. you can separate your calulations by line and pass the values by using the = operator to declare the results of a calulcation as a new named value

#when done correct this is how it will look below. 
# EXCHANGE_RATE = 1.20
# BUDGET = 127.25
# SPREAD = 10
# DENOMINATION = 5

def exchangeable_value(budget, exchange_rate, spread, denomination):
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    adjusted_exchange_rate = exchange_rate*(1+spread/100)
    exchanged_amount=budget / adjusted_exchange_rate
    max_value = (int(exchanged_amount) // denomination) * denomination
    return max_value
    pass

# Prompting for user input
budget = float(input("Enter your budget: "))
exchange_rate = float(input("Enter the exchange rate: "))
spread = int(input("Enter the spread (as an integer percentage): "))
denomination = int(input("Enter the currency denomination: "))

# Calling the function with user inputs
result = exchangeable_value(budget, exchange_rate, spread, denomination)

print(f"Maximum value you can get: {result}")

while True:  # This starts an infinite loop
    try:
        budget = input("Enter your budget (or type 'exit' to quit): ")
        if budget.lower() == 'exit':  # User can type 'exit' to break the loop
            break
        budget = float(budget)

        exchange_rate = float(input("Enter the exchange rate: "))
        spread = int(input("Enter the spread (as an integer percentage): "))
        denomination = int(input("Enter the currency denomination: "))

        result = exchangeable_value(budget, exchange_rate, spread, denomination)
        print(f"Maximum value you can get: {result}\n")
    except ValueError:  # Catches any conversion errors
        print("Please enter valid numbers. Try again.\n")

print("Application exited.")