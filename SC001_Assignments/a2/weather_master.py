"""
File: weather_master.py
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

EXIT = -100
# placeholder for highest and lowest temp
UNDEFINED = -200


def main():
    """
    This program calculates the highest temp, the lowest temp, displays average of the entered temps,
    as well as the amount of cold days. Cold days are defined as temps less than 16.
    """
    print('stanCode "Weather Master 4.0"!')
    weather_highest = UNDEFINED
    weather_lowest = UNDEFINED
    weather_input = -200
    cds = 0
    temp_count = 0
    temp_sum = 0
    if weather_input == EXIT:
        print('No temperatures were entered.')
    while True:
        weather_input = float(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
        # initialize highest temp
        if weather_highest == UNDEFINED:
            weather_highest = weather_input
        # initialize lowest temp
        if weather_lowest == UNDEFINED:
            weather_lowest = weather_input
        # identify highest & lowest & when to exit
        if weather_input == EXIT:
            break
        elif weather_input > weather_highest:
            weather_highest = weather_input
        elif weather_input < weather_lowest:
            weather_lowest = weather_input
        # count no. of cold days
        if weather_input < 16:
            cds += 1
        # counts the amount of temperatures entered
        temp_count += 1
        # sums up the total temperatures entered
        temp_sum += weather_input
    print(str(cds) + ' Cold Days')
    # averages the temperatures entered
    print('Average = ' + str(temp_sum/temp_count))
    print('Lowest Temperature is ' + str(int(weather_lowest)))
    print('Highest Temperature is ' + str(int(weather_highest)))


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
