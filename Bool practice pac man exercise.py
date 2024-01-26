"""Functions for implementing the rules of the classic arcade game Pac-Man."""


def eat_ghost(power_pellet_active, touching_ghost):
    """Verify that Pac-Man can eat a ghost if he is empowered by a power pellet.

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - can the ghost be eaten?
    """
    return power_pellet_active and touching_ghost
    


def score(touching_power_pellet, touching_dot):
    """Verify that Pac-Man has scored when a power pellet or dot has been eaten.

    :param touching_power_pellet: bool - is the player touching a power pellet?
    :param touching_dot: bool - is the player touching a dot?
    :return: bool - has the player scored or not?
    """
    return touching_power_pellet or touching_dot
    


def lose(power_pellet_active, touching_ghost):
    """Trigger the game loop to end (GAME OVER) when Pac-Man touches a ghost without his power pellet.

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - has the player lost the game?
    """
    return touching_ghost and not power_pellet_active
    


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """Trigger the victory event when all dots have been eaten.

    :param has_eaten_all_dots: bool - has the player "eaten" all the dots?
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - has the player won the game?
    """
    return has_eaten_all_dots and (not touching_ghost or (touching_ghost and power_pellet_active))
    
# # prompting for user input
# has_eaten_all_dots = input("Has Pac Man Eaten all of the Dots?")
# power_pellet_active = input("Does Pac Man have a power pellet active?")
# touching_ghost = input("Is Pac Man touching a ghost?")

# # Calling the function with user inputs
# result = win(has_eaten_all_dots, power_pellet_active, touching_ghost)

# print(f"Did Pac Man win the game?: {result}")

while True: #This starts and infinite loop
    try:
        has_eaten_all_dots_input = input("Enter whether Pac Man has eaten all the dots(yes/no) (or type 'exit' to quit): ")
        if has_eaten_all_dots_input.lower() == 'exit':  # User can type 'exit' to break the loop
            break

        power_pellet_active_input = input("Is the power pellet active? (yes/no): ")
        if power_pellet_active_input.lower() == 'exit':
            break

        touching_ghost_input = input("Is Pac Man touching a ghost? (yes/no): ")
        if touching_ghost_input.lower() == 'exit':
            break

        # Convert inputs to boolean
        has_eaten_all_dots = has_eaten_all_dots_input.lower() == 'yes'
        power_pellet_active = power_pellet_active_input.lower() == 'yes'
        touching_ghost = touching_ghost_input.lower() == 'yes'

        result = win(has_eaten_all_dots, power_pellet_active, touching_ghost)
        print(f"Did Pac Man win the game?: {result}\n")
    except ValueError:
        print("Invalid Input. Please enter yes, or no, or exit")

print("Application Closed")
