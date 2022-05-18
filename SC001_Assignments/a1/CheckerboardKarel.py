from karel.stanfordkarel import *

"""
File: CheckerboardKarel.py
Name: Will Chang
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


def main():
    """
    Pre-condition: Karel is facing east at Street 1 Avenue 1 with no beepers on the board
    Post-condition: Karel is facing east at Street 8 Avenue 8 with checkered board (beepers covering the baord)
    """
    the_one_function()


def the_one_function():
    for i in range(39):
        fill_checkerboard()
    karel_pigeon_mode()


def karel_pigeon_mode():
    """
    Pre-condition: Karel is facing east at Street 3 Avenue 3
    Post-condition: Karel is facing east at Street 8 Avenue 8
    """
    while front_is_clear():
        move()
        if not front_is_clear():
            turn_left()
            while front_is_clear():
                move()
                if not front_is_clear():
                    if not right_is_clear():
                        turn_right()


def fill_checkerboard():
    """
    Pre-condition: Karel is facing east at Street 1 Avenue 1
    Post-condition: Karel is facing east at Street 3 Avenue 3
    """
    if front_is_clear():
        move()
        if not on_beeper():
            turn_around()
            move()
            if not on_beeper():
                put_beeper()
            turn_around()
            move()
            if front_is_clear():
                move()
            else:
                turn_left()
                move()
        if on_beeper():
            turn_around()
            move()
            turn_right()
            move()
    if not front_is_clear():
        turn_left()


def turn_right():
    for i in range(3):
        turn_left()


def turn_around():
    for i in range(2):
        turn_left()


####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)
