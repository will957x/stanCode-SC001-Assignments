"""
File: mirror_lake.py
Name: Will Chang
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


"""
This program creates a new blank image that is twice the height of the original image.
Then the program takes the original image and copies it onto the new blank image as is.
Finally, the program takes the original pixels and reflects it across the y axis.
"""


def reflect(filename):
    img = SimpleImage("images/mt-rainier.jpg")
    blank_img = SimpleImage.blank(img.width, img.height*2)
    blank_img.show()
    for x in range(img.width):
        for y in range(img.height):
            old_pixel = img.get_pixel(x, y)

            new_pixel1 = blank_img.get_pixel(x, y)
            new_pixel2 = blank_img.get_pixel(x, blank_img.height-1-y)

            new_pixel1.red = old_pixel.red
            new_pixel1.green = old_pixel.green
            new_pixel1.blue = old_pixel.blue

            new_pixel2.red = old_pixel.red
            new_pixel2.green = old_pixel.green
            new_pixel2.blue = old_pixel.blue
    return blank_img


def main():
    original_mt = SimpleImage("images/mt-rainier.jpg")
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
