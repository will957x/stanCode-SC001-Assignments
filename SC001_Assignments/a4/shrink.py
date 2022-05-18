"""
File: shrink.py
Name: Will Chang
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    img = SimpleImage("images/poppy.png")
    blank_img = SimpleImage.blank(img.width//2, img.height//2)
    for x in range(img.width//2):
        for y in range(img.height//2):
            old_pixel = img.get_pixel(x*2, y*2)
            new_pixel = blank_img.get_pixel(x, y)
            new_pixel.red = old_pixel.red
            new_pixel.green = old_pixel.green
            new_pixel.blue = old_pixel.blue
    return blank_img


def main():
    """
    This program shrinks the image by creating a new blank image that is half the height and width of the original image.
    Then it targets half of the pixels and only takes the even coordinates of the pixels, which effectively shrinks
    the image by a quarter of its original size.
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


if __name__ == '__main__':
    main()
