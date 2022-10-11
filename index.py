import math
print("hello")
a = int(input("insert number a"))
b = int(input("insert number b"))
c = int(input("insert number c"))


descriminant = (b*b) - (4*a*c)

if descriminant > 0:
    root1 = math.floor(((-b + math.sqrt(descriminant))/(2*a)))
    root2 = math.floor(((-b - math.sqrt(descriminant))/(2*a)))
    print("the roots of the equation are " f'{root1}' " and " f'{root2}')
elif descriminant == 0:
    root1 = root2 = math.floor(-b / (2*a))
    print("the roots of the equations are the same and is " f'{root1}')
else:
    print("The equation has no real root")
