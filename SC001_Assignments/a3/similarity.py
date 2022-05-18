"""
File: similarity.py
Creator: Will Chang
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""

def main():
    ls1 = long_sequence()
    ss1 = short_sequence()
    compare_sequences(ls1, ss1)


def compare_sequences(ls2, ss2):
    ans = ''
    maximum = 0
    for j in range(len(ls2)-len(ss2)+1):
        compare = ls2[j:len(ss2)+j]
        matched = 0
        for i in range(len(ss2)):
            if ss2[i] == compare[i]:
                matched += 1
                if matched > maximum:
                    maximum = matched
                    ans = compare
    print(ans)


def short_sequence():
    ss = input('What DNA sequence would you like me to match? ')
    ss = ss.upper()
    return ss


def long_sequence():
    ls = input('Please give me a DNA sequence to search: ')
    ls = ls.upper()
    return ls

###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
