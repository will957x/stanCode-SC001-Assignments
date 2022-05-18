"""
File: hailstone.py
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    This program carries out the Hailstone sequence by dividing the input by 2 when the input is even
    and multiplying the input by three and then adding one if the input is odd.
    This program also records the number of steps taken to reach 1.
    """
    print('This program completes the Hailstone sequence')
    n = int(input('Enter a number: '))
    steps = 0
    while n != 1:
        steps += 1
        # This step identifies the input as even
        if n % 2 == 0:
            print(str(int(n)) + ' is even, so I take half: ' + str(int(n/2)))
            # this adds back the new value of the input after dividing it by 2
            n /= 2
            # this adds the number of steps
        elif n % 2 == 1:
            print(str(int(n)) + ' is odd, so I take make 3n+1: ' + str(int(3*n+1)))
            # this adds back the new value of the input after multiplying the input by three then adding one
            n = 3*n+1
    print('It took ' + str(steps) + ' steps to reach 1.')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
