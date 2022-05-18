"""
File: green_screen.py
Name: Will Chang
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in "ReyGreenScreen.png".
"""

from simpleimage import SimpleImage


THRESHOLD = 1.3
BLACK_PIXEL = 100


"""
This program takes the original image of the character in the green screen and imports the background of a spaceship
into the image. The program also resizes the spaceship background to fit the size of the character. 
"""


def combine(background_img, figure_img):
    for y in range(background_img.height):
        for x in range(background_img.width):
            new_pixel = figure_img.get_pixel(x, y)
            avg = (new_pixel.red+new_pixel.blue+new_pixel.green) // 3
            total = new_pixel.red+new_pixel.blue+new_pixel.green
            if new_pixel.green > avg*THRESHOLD and total > BLACK_PIXEL:
                pixel_bg = background_img.get_pixel(x, y)
                new_pixel.red = pixel_bg.red
                new_pixel.blue = pixel_bg.blue
                new_pixel.green = pixel_bg.green
    return figure_img


def main():
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()
