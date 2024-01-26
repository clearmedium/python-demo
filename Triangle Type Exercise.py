##1

def equilateral(sides):

    if sides[0] == 0 and sides[1] == 0 and sides[2] == 0:
        return False
    elif sides[0] == sides[1] and sides[0] == sides[2]:
        return True
    return False


##2

def isosceles(sides):

    if equilateral(sides) == True:
        return True
    elif sides[0] == sides[1] and sides[0] + sides[1] > sides[2]:
        return True
    elif sides[1] == sides[2] and sides[1] + sides[2] > sides[0]:
        return True
    elif sides[0] == sides[2] and sides[0] + sides[2] > sides[1]:
        return True
    else:
        return False




##3


def scalene(sides):
    is_a_triangle = sides[0] + sides[1] > sides[2] and sides[1] + sides[2] > sides[0] and sides[0] + sides[2] > sides[1]

    if equilateral(sides) == True:
        return False
    if isosceles(sides) == True:
        return False
    if is_a_triangle == False:
        return False
    elif sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2]:
        return True
    pass
