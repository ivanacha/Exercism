def isTriangle(sides):
    sides.sort()
    a, b, c = sides
    if a == 0:
            return False
    if a + b >= c:
        return True
    return False
    
def equilateral(sides):
    return isTriangle(sides) and len(set(sides)) == 1


def isosceles(sides):
    return isTriangle(sides) and len(set(sides)) <= 2


def scalene(sides):
    return isTriangle(sides) and len(set(sides)) == 3
