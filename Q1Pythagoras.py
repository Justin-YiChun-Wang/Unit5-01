import math
print('please enter the length of the first side of the triangle')
a = float(input())
print('please enter the length of the second side of the triangle')
b = float(input())
c2 = a ** 2 + b ** 2
c = math.sqrt(c2)
print('The length of hypotenuse is', c)
