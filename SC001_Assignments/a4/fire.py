"""
File: fire.py
Name: Will Chang
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    This program takes the original image and checks whether the pixel is above or below the hurdle factor.
    If the pixel is more than the hurdle factor times the average, the red is amplified into 255.
    If the pixel is less than the hurdle factor times the average, the pixel is rendered grey.
    """
    img = SimpleImage("images/greenland-fire.png")
    for pixel in img:
        avg = (pixel.red + pixel.green + pixel.blue) // 3
        if pixel.red > avg * HURDLE_FACTOR:
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        if pixel.red < avg * HURDLE_FACTOR:
            pixel.red = avg
            pixel.green = avg
            pixel.blue = avg
    return img


def main():
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()



if __name__ == '__main__':
    main()
