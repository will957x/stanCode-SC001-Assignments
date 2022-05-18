"""
File: hangman.py
Creator: Will Chang
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This function runs a game of hangman by first importing the random_word function into the variable "word."
    The constant "N_Turns" is imported into the variable of "turns."
    The user's input is imported into the variable "guess."
    The program looks for the user's "guess" within "word" and if found the system would would return an output
    of an integer other than -1 and print "You are correct!"
    The program will then restring the word by looking for the guessed letter in each of the letters within word,
    and if found, it will add it to "result", which is an empty string, and add '-' to the rest of "result."
    The program will then save the result into the variable "current".
    On next loop, the program will check the guessed letter  against the saved "current" string,
    if there are letters in current, the letter will be added to the new result string and if there are not letters,
    '-' will be added to the new result string
    The program will print "You win!" and "The word was: (insert word)".
    Lastly, the constant "N_Turns" is captured by the variable "turns" and each time an incorrect guess is given,
    the count will go up so if turns reach 0, the program will terminate.
    """
    word = random_word()
    current = str(len(word) * '-')
    print('The word looks like: ' + current)
    turns = N_TURNS
    guess = get_guess()
    while True:
        if turns > 0:
            if word.find(guess) != -1:
                print('You are correct! ')
                result = ''
                index_no = word.find(guess)
                if index_no != -1:
                    for i in range(len(word)):
                        ch = word[i]
                        if ch == guess:
                            result += guess
                        else:
                            if current[i] != '-':
                                result += current[i]
                            else:
                                result += '-'
                current = result
                print(current)
                if current == word:
                    print('You win!\n' + 'The word was: ' + str(word))
                    break
                else:
                    print('You have ' + str(turns) + ' left')
                    guess = get_guess()
            else:
                print('There are no ' + str(guess) + "'s in the word.")
                print('The word looks like: ' + str(current))
                print('You have ' + str(turns) + ' left')
                turns -= 1
                guess = get_guess()
        else:
            print('You are completely hung :(')
            print('The word was: ' + str(word))
            break


def get_guess():
    """
    This functions gets the input from the user and is captured by the "guess" variable.
    This function also checks if guess is legal by checking against if the letter entered is more than 1 or if
    the user entered a non-letter.
    :return:
    """
    guess = input('Your guess: ')
    guess = guess.upper()
    if guess.isdigit():
        print('Illegal Format ')
    elif len(guess) > 1:
        print('Illegal Format')
    return guess


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
