from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
Name: Will Chang
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""


def main():
    """
    Pre-condition: Karel is facing east at Street 1 Avenue 1 before fixing the columns
    Post-condition: Karel is facing east at Street 1 Avenue 13 having fixed the columns of Avenues 1,5,9,13
    """
    rebuild_all()


def rebuild_all():
    for i in range(3):
        rebuild_pillars()
        next_pillar()
    rebuild_pillars()
    turn_around()
    for i in range(4):
        move()
    turn_left()


def next_pillar():
    """
    Pre-condition: Karel is facing north at top of column at Street 5 Avenue 1 or at the top of the respective column
    Post-condition: Karel is at the bottom of the next column at Street 1 Avenue 5 (or the next respective column)
    """
    if not front_is_clear():
        turn_right()
        for i in range(4):
            move()
        turn_right()
        for i in range(4):
            move()
        turn_left()


def turn_around():
    for i in range(2):
        turn_left()


def rebuild_pillars():
    """
    Pre-condition: Karel is  facing east at Street 1 Avenue 1 (or at bottom of respective columns)
    Post-condition: Karel is facing north at Street 5 Avenue 1 (or at top of respective columns) after rebuilding the column
    """
    turn_left()
    while front_is_clear():
        if not on_beeper():
            put_beeper()
        move()
    else:
        if not front_is_clear():
            if not on_beeper():
                put_beeper()


def turn_right():
    for i in range(3):
        turn_left()


####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)
