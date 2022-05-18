from karel.stanfordkarel import *

"""
File: MidpointKarel.py
Name: Will Chang
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def main():
    """
    Pre-condition: Karel is facing east at Street 1 Avenue 1
    Post-condition: Karel is at midpoint on a beeper facing east, in the case of the 5x5 parameter, this is at Street 1 Avenue 3
    """
    mapping()
    pinpoint()
    triangulate()
    midpoint()
    """
    Extra notes: The way I wanted to approach this midpoint issue was through establishing my own parameters.
    Since parameter limitation via command is through whether "front is clear" I had to set up new parameters with beepers.
    Once I have new parameters through setting up the beepers, I moved to narrow down the range between the beepers by bouncing Karel back and forth between two beepers.
    The last limitation I set was if Karel encountered another beeper on the space next to a beeper, Karel will know a midpoint has been reached and should pick up that beeper and return to the previous beeper.
    Karel can now find the midpoint from parameters ranging from 5x5 to 40x40. Cheers.
    """


def midpoint():
    """
    Pre-condition: Karel is facing west at Street 1 Avenue 2 on beeper
    Post-condition: Karel is facing east at Street 1 Avenue 3 after picking up the beeper on the left of midpoint, in this case this is at Street 1 Avenue 2
    """
    if on_beeper():
        turn_around()
        move()
        if on_beeper():
            turn_around()
            move()
            pick_beeper()
            turn_around()
            move()


def triangulate():
    """
    Pre-condition: Karel is facing east on the left-most beeper at Street 1 Avenue 2
    Post-condition: Karel is facing west at Street 1 Avenue 2 on a beeper, after picking up beeper at Street 1 Avenue 4 and after placing a new beeper at Street 1 Avenue 3
    """
    if on_beeper():
        move()
        while not on_beeper():
            move()
            if on_beeper():
                turn_around()
                pick_beeper()
                move()
                put_beeper()
                move()


def pinpoint():
    """
    Pre-condition: Karel is facing west at Street 1 Avenue 4 having placed a beeper at Street 1 Avenue 2 and Street 1 Avenue 4, respectively
    Post-condition: Karel is facing east on the left-most beeper, in 5x5 scenario this is the beeper at Street 1 Avenue 2
    """
    if on_beeper():
        move()
        while not on_beeper():
            move()
            if on_beeper():
                turn_around()


def mapping():
    """
    Pre-condition: Karel is facing east at Street 1 Avenue 1
    Post-condition: Karel is facing west at Street 1 Avenue 4 having placed a beeper at Street 1 Avnue 2 and Street 1 Avenue 4 respectively
    """
    move()
    put_beeper()
    while front_is_clear():
        move()
    if not front_is_clear():
        turn_around()
        move()
        put_beeper()


def turn_around():
    for i in range(2):
        turn_left()


####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)
