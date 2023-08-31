
print(" Hello, NIrajan Prajapati !")
print("")


" q.no. 2.1"
vars_name=input("Enter your name = ")
print("Hello, " + vars_name + "!")


#Write a program that asks the user for the radius of a circle and the prints out the area of the circle.

import math

vars_radius=float(input("Enter radius of circle = "))
vars_area= 2 * math.pi * vars_radius
print(vars_area)


#Write a program that asks the user for the length and width of a rectangle. The program then prints out the perimeter and area of the rectangle. The perimeter of a rectangle is the sum of the lengths of each four sides.

import math
vars_length=float(input(" length of the rectangle = "))
vars_breadth=float(input(" breath of the rectangle = "))
vars_area= vars_length * vars_breadth
vars_perimeter=2*(vars_length + vars_breadth)
print("The area is ",  vars_area)
print("perimeter of rectangle ",vars_perimeter)


#Write a program that asks the user for three integer numbers. The program prints out the sum, product, and average of the numbers.

vars_a=int(input("a = "))
vars_b=int(input("b = "))
vars_c=int(input("C = "))
vars_sum= vars_a + vars_b +vars_c
vars_multiply= vars_a*vars_b*vars_c
vars_avg=(vars_a+vars_b+vars_c)/3
print("sum of a,b,c =", vars_sum)
print("product of a,b,c =" , vars_multiply)
print("average of a,b,c =",vars_avg)



#Write a program that draws two random combinations of numbers for a combination lock:
# 1. a 3-digit code where each number is between 0 and 9.
# 2: a 4-digit code where each number is between 1 and 6.


import random

digit3 = [random.randint(0, 9) for _ in range(3)]
digit4 = [random.randint(1, 6) for _ in range(4)]

print("3-Digit Code:", ''.join(map(str, digit3)))
print("4-Digit Code:", ''.join(map(str, digit4)))


# Write a program that asks the user to enter a mass in medieval units: talents (leiviskä), pounds (naula), and lots (luoti). The program converts the input to full kilograms and grams and outputs the result to the user:
POUNDS_PER_TALENT = 20
LOTS_PER_POUND = 32
GRAMS_PER_LOT = 13.3
GRAMS_PER_KILOGRAM = 1000

talents = float(input("Enter mass in talents: "))
pounds = float(input("Enter mass in pounds: "))
lots = float(input("Enter mass in lots: "))

total_grams = (talents * POUNDS_PER_TALENT + pounds) * LOTS_PER_POUND * GRAMS_PER_LOT + lots * GRAMS_PER_LOT

kilograms = int(total_grams / GRAMS_PER_KILOGRAM)
remaining_grams = total_grams % GRAMS_PER_KILOGRAM

print(f"The mass is approximately: {kilograms} kilograms and {remaining_grams} grams")

