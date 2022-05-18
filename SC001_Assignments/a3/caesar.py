"""
File: caesar.py
Creator: Will Chang
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    This program gets input by the user for a codeword, which is a number for decryption,
    and a ciphered string, which is an encrypted string of letters.
    This program subsequently decodes the encrypted ciphered string through shifting the
    letters of the ciphered string individually by amount as informed in the codeword input.
    This program is also case-insensitive and leaves non-alphabets as is, which includes
    "space" and symbols.

    In addition: this program can be used to encode messages by following the steps above but in reverse
    by entering an unencrypted ciphered string to be encrypted by the codeword.
    To decrypt the message, one must enter a "reverse codeword" so 3 would be -3.
    E.g. encrypting "Pokémon! Gotta Catch ‘Em All!" with 3 as the codeword would yield "SRNÉPRQ! JRWWD FDWFK ‘HP DOO!"
    This ciphered string can be decoded using -3!
    """
    # encapsulates the codeword function, which will be used to decrypt the encrypted word(s)
    ShiftNum = codeword()
    # the encrypted string
    CipherString = input("What's the ciphered string? ")
    # makes encrypted string case insensitive
    CipherString = CipherString.upper()
    new_alphabet(ShiftNum, CipherString)

    
def new_alphabet(ShiftNum1, CipherString1):
    """
    :param ShiftNum1: the number we want to shift by
    :param CipherString1: the ciphered string we inputted
    :return: the ciphered string after decrypting by the number we want and restringing onto "result"
    """
    result = ''
    for i in range(len(CipherString1)):
        old_char = CipherString1[i]
        newchar = shiftchar(old_char, ShiftNum1)
        result += newchar
    print(result)


def shiftchar(Old_Char2, ShiftNum2):
    """
    :param old_char2: the ciphered string inputted
    :param ShiftNum2: the number we want to shift the letters inputted
    :return: the ciphered string after shifting by the number we inputted, and leaving
    non-alphabets such as "space" and symbols as is
    """
    for i in range(len(ALPHABET)):
        n = i + ShiftNum2
        # determines where the alphabet is in the original order
        if ALPHABET[i] == Old_Char2:
            # when index exceeds 26, must wrap around and start from 0 again to be within index range
            if n >= 26:
                n = i + ShiftNum2 - 26
            # when code entered is negative, must add 26 to be within index range
            elif n < 0:
                n += 26
            return ALPHABET[n]
    # returns all not found in ALPHABET as is, so "space" and symbols such as "!" will be returned
    else:
        return Old_Char2


def codeword():
    # creates the codeword later used for decryption
    x = int(input('Secret Number: '))
    return x


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
