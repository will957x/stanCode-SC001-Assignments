from karel.stanfordkarel import *

"""
File: CollectNewspaperKarel.py
Name: Will Chang
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""


def main():
    """
    Pre-condition: Karel is facing east without beeper (newspaper) at Street 4 Avenue 3
    Post-condition: Karel is facing east with beeper (newspaper) at Street 4 Avenue 3
    """
    collect_newspaper()
    carry_newspaper_home()


def collect_newspaper():
    """
    Pre-condition: Karel is facing east without beeper (newspaper) at Street 4 Avenue 3
    Post-condition: Karel is facing east and has collected the beeper (newspaper) at Street 3 Avenue 6
    """
    if not on_beeper():
        for i in range(2):
            move()
        turn_right()
        move()
        turn_left()
        move()
        pick_beeper()


def turn_right():
    for i in range(3):
        turn_left()


def turn_around():
    for i in range(2):
        turn_left()


def carry_newspaper_home():
    """
    Pre-condition: Karel is facing east without the beeper (newspaper) at Street 3 Avenue 6
    Post-condition: Karel is facing east with beeper (newspaper) at Street 4 Avenue 3
    """
    turn_around()
    move()
    turn_right()
    move()
    turn_left()
    move()
    move()
    turn_around()
    put_beeper()

####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)
