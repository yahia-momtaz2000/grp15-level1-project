# program to calculate perimeter and area of a circle
# inputs
import math

radius = 7

# area
# pow : it is a builtin function in the built in module math
print(math.pi)
area = math.pi * math.pow(radius, 2)
area = round(area, 2)
print(area)
print('--------- perimeter ----------------')
perimeter = 2 * math.pi * radius
perimeter = round(perimeter, 2)
print(perimeter)


