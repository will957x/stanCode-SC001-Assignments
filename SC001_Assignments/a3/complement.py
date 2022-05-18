"""
File: complement.py
Creator: Will Chang
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    dna = input("Please give me a DNA strand and I'll find the complement: ")
    # makes dna case insensitive by converting all input to upper case
    dna = dna.upper()
    newdna = build_complement(dna)
    print('The DNA of ' + dna + ' is ' + newdna)


def build_complement(dna):
    """
    param: outputs particular upper case letters when matching ones are entered
    such as outputting A when inputting T and so on
    return: uppercase of entered letters that include t, a, c, g
    """
    ans = ''
    for base in dna:
        if base == 'T':
            ans += 'A'
        elif base == 'A':
            ans += 'T'
        elif base == 'C':
            ans += 'G'
        elif base == 'G':
            ans += 'C'
    return ans


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
