"""
File: quadratic_solver.py
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	This program calculates the entered variables to see if there are 2, 1, or 0 real roots,
	as defined in the quadratic equation. This program also uses the discriminant function to
	identify whether there are 2, 1, or 0 real roots.
	"""
	print('stanCode Quadratic Solver! ')
	a = float(input('Enter a: '))
	b = float(input('Enter b: '))
	c = float(input('Enter c: '))
	x = (b**2)-(4*a*c)
	# if discriminant is less than 0 the output is no real roots
	if x < 0:
		print('No real roots ')
	elif x >= 0:
		y = math.sqrt(x)
		x1 = (-b+y)/(2*a)
		x2 = (-b-y)/(2*a)
		# if the discriminant is equal to 0, the output is one root and the root is displayed
		if x == 0:
			print('One root: ' + str(x1))
		# if the discriminant is bigger than 0, the output is two root and the roots are displayed
		else:
			print('Two roots: ' + str(x1) + ', ' + str(x2))


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
