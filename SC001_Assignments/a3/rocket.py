"""
File: rocket.py
Creator: Will Chang
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant determines rocket size
SIZE = 3


def main():
	"""
	This program prints a rocket as determined by the constant (SIZE).
	"""
	head(SIZE)
	belt(SIZE)
	upper(SIZE)
	lower(SIZE)
	belt(SIZE)
	head(SIZE)


def lower(variable):
	# reverses fuel so that the first layer starts with no fuel ('.')
	s = -1
	# reverses support so that it starts higher than the variable, which the program will then minus by 1 in each loop
	y = variable+1
	# the edget of the body is a constant output so 1 represents this
	x = 1
	edge = x*'|'
	for i in range(variable):
		s += 1
		# fuel refers to the "." in the body of the rocket
		fuel = s*'.'
		# decreases y, which is the "\/", by 1 in each loop
		y -= 1
		# shape of lower half of the body
		support = y*('\\'+'/')
		print(edge + fuel + support + reverse(fuel) + reverse(edge))


# upper half of the body of the rocket
def upper(variable):
	s = variable
	y = 0
	x = 1
	edge = x*'|'
	for i in range(variable):
		s -= 1
		# fuel refers to the "." in the body of the rocket
		fuel = s*'.'
		# increases y, which is the "/\", by 1 in each loop
		y += 1
		support = y*('/'+'\\')
		print(edge + fuel + support + reverse(fuel) + reverse(edge))


def belt(variable):
	s = variable
	x = 1
	# determines the belt by constructing 1 "+" combined with the "=" multiplied by the constant
	result = (x*'+'+s*'=')
	# prints both sides of the belt
	print(result+reverse(result))


def head(variable):
		s = variable
		x = 0
		for i in range(variable):
			s -= 1
			x += 1
			# pushes the entire print output to the right by 1 "space" so it aligns with the best
			result_space = (' ')
			# determines the right half of the "head"
			result = (s * ' ' + x * '/')
			# determines the left half of the "head"
			result_2 = (s * ' ' + x * '\\')
			print(result_space + result + reverse(result_2))


def reverse(variable):
	"""
	:param variable: The variable to be reversed
	:return result: The reversed string
	"""
	result = ''
	for i in range(len(variable)):
		# reverses the sequence of the variable
		result = variable[i] + result
	return result


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()