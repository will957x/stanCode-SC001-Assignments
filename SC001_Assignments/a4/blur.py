"""
File: blur.py
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


"""
This program blurs the image by dividing the target areas into three sections.
The first section is the four corners of the photo, which has 4 surrounding pixels.
The second section is the four bordering units, which has 6 surrounding pixels.
The third section, which is the "else" section, refers to the regular condition where 9 pixels surround the targeted pixel.
The program then takes the surrounding pixels (either 4,6, or 9), averages them, and then inserts them back to the targeted pixel.
The resulting image is blurred.
"""


def blur(img):
    blank_img = SimpleImage.blank(img.width, img.height)
    for x in range(blank_img.width):
        for y in range(blank_img.height):
            blank_pixel = blank_img.get_pixel(x, y)
            # upper left corner pixel
            if (x, y) == (0, 0):
                pixel1 = img.get_pixel(x, y)
                pixel2 = img.get_pixel(x + 1, y)
                pixel3 = img.get_pixel(x, y + 1)
                pixel4 = img.get_pixel(x + 1, y + 1)
                blank_pixel.red = (pixel1.red + pixel2.red + pixel3.red + pixel4.red)//4
                blank_pixel.green = (pixel1.green + pixel2.green + pixel3.green + pixel4.green)//4
                blank_pixel.blue = (pixel1.blue + pixel2.blue + pixel3.blue + pixel4.blue)//4
            # upper right corner pixel
            elif (x, y) == (blank_img.width-1, 0):
                pixel1 = img.get_pixel(x, y)
                pixel2 = img.get_pixel(x - 1, y)
                pixel3 = img.get_pixel(x, y + 1)
                pixel4 = img.get_pixel(x - 1, y + 1)
                blank_pixel.red = (pixel1.red + pixel2.red + pixel3.red + pixel4.red) // 4
                blank_pixel.green = (pixel1.green + pixel2.green + pixel3.green + pixel4.green) // 4
                blank_pixel.blue = (pixel1.blue + pixel2.blue + pixel3.blue + pixel4.blue) // 4
            # bottom left corner pixel
            elif (x, y) == (0, blank_img.height-1):
                pixel1 = img.get_pixel(x, y - 1)
                pixel2 = img.get_pixel(x + 1, y - 1)
                pixel3 = img.get_pixel(x + 1, y)
                pixel4 = img.get_pixel(x, y)
                blank_pixel.red = (pixel1.red + pixel2.red + pixel3.red + pixel4.red) // 4
                blank_pixel.green = (pixel1.green + pixel2.green + pixel3.green + pixel4.green) // 4
                blank_pixel.blue = (pixel1.blue + pixel2.blue + pixel3.blue + pixel4.blue) // 4
            # bottom right corner pixel
            elif (x, y) == (blank_img.height - 1, blank_img.width - 1):
                pixel1 = img.get_pixel(x, y)
                pixel2 = img.get_pixel(x - 1, y)
                pixel3 = img.get_pixel(x - 1, y - 1)
                pixel4 = img.get_pixel(x, y - 1)
                blank_pixel.red = (pixel1.red + pixel2.red + pixel3.red + pixel4.red) // 4
                blank_pixel.green = (pixel1.green + pixel2.green + pixel3.green + pixel4.green) // 4
                blank_pixel.blue = (pixel1.blue + pixel2.blue + pixel3.blue + pixel4.blue) // 4

            # left border
            elif x == 0 and 0 < y < blank_img.height -1:
                pixel1 = img.get_pixel(x, y)
                pixel2 = img.get_pixel(x, y - 1)
                pixel3 = img.get_pixel(x + 1, y - 1)
                pixel4 = img.get_pixel(x + 1, y)
                pixel5 = img.get_pixel(x + 1, y + 1)
                pixel6 = img.get_pixel(x, y + 1)
                blank_pixel.red = (pixel1.red + pixel2.red + pixel3.red + pixel4.red + pixel5.red + pixel6.red) // 6
                blank_pixel.green = (pixel1.green + pixel2.green + pixel3.green + pixel4.green + pixel5.green + pixel6.green) // 6
                blank_pixel.blue = (pixel1.blue + pixel2.blue + pixel3.blue + pixel4.blue + pixel5.blue + pixel6.blue) // 6
            # top border
            elif y == 0 and 0 < x < blank_img.width -1:
                pixel1 = img.get_pixel(x, y)
                pixel2 = img.get_pixel(x + 1, y)
                pixel3 = img.get_pixel(x + 1, y + 1)
                pixel4 = img.get_pixel(x, y + 1)
                pixel5 = img.get_pixel(x - 1, y + 1)
                pixel6 = img.get_pixel(x - 1, y)
                blank_pixel.red = (pixel1.red + pixel2.red + pixel3.red + pixel4.red + pixel5.red + pixel6.red) // 6
                blank_pixel.green = (pixel1.green + pixel2.green + pixel3.green + pixel4.green + pixel5.green + pixel6.green) // 6
                blank_pixel.blue = (pixel1.blue + pixel2.blue + pixel3.blue + pixel4.blue + pixel5.blue + pixel6.blue) // 6
            # right border
            elif x == blank_img.width-1 and 0 < y < blank_img.width -1:
                pixel1 = img.get_pixel(x, y)
                pixel2 = img.get_pixel(x, y + 1)
                pixel3 = img.get_pixel(x - 1, y)
                pixel4 = img.get_pixel(x - 1, y - 1)
                pixel5 = img.get_pixel(x - 1, y - 1)
                pixel6 = img.get_pixel(x, y - 1)
                blank_pixel.red = (pixel1.red + pixel2.red + pixel3.red + pixel4.red + pixel5.red + pixel6.red) // 6
                blank_pixel.green = (pixel1.green + pixel2.green + pixel3.green + pixel4.green + pixel5.green + pixel6.green) // 6
                blank_pixel.blue = (pixel1.blue + pixel2.blue + pixel3.blue + pixel4.blue + pixel5.blue + pixel6.blue) // 6
            # bottom border
            elif y == blank_img.height - 1 and 0 < x < blank_img.width - 1:
                pixel1 = img.get_pixel(x, y)
                pixel2 = img.get_pixel(x - 1, y)
                pixel3 = img.get_pixel(x - 1, y - 1)
                pixel4 = img.get_pixel(x, y - 1)
                pixel5 = img.get_pixel(x + 1, y - 1)
                pixel6 = img.get_pixel(x + 1, y)
                blank_pixel.red = (pixel1.red + pixel2.red + pixel3.red + pixel4.red + pixel5.red + pixel6.red) // 6
                blank_pixel.green = (pixel1.green + pixel2.green + pixel3.green + pixel4.green + pixel5.green + pixel6.green) // 6
                blank_pixel.blue = (pixel1.blue + pixel2.blue + pixel3.blue + pixel4.blue + pixel5.blue + pixel6.blue) // 6
            # regular scenarios
            else:
                pixel1 = img.get_pixel(x, y)
                pixel2 = img.get_pixel(x, y - 1)
                pixel3 = img.get_pixel(x + 1, y - 1)
                pixel4 = img.get_pixel(x + 1, y)
                pixel5 = img.get_pixel(x + 1, y + 1)
                pixel6 = img.get_pixel(x, y + 1)
                pixel7 = img.get_pixel(x - 1, y + 1)
                pixel8 = img.get_pixel(x - 1, y)
                pixel9 = img.get_pixel(x - 1, y - 1)
                blank_pixel.red = (pixel1.red + pixel2.red + pixel3.red + pixel4.red + pixel5.red + pixel6.red + pixel7.red + pixel8.red + pixel9.red) // 9
                blank_pixel.green = (pixel1.green + pixel2.green + pixel3.green + pixel4.green + pixel5.green + pixel6.green + pixel7.green + pixel8.green + pixel9.green) // 9
                blank_pixel.blue = (pixel1.blue + pixel2.blue + pixel3.blue + pixel4.blue + pixel5.blue + pixel6.blue + pixel7.blue + pixel8.blue + pixel9.blue) // 9
    return blank_img

def main():
    """
    TODO:
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)

    blurred_img.show()


if __name__ == '__main__':
    main()
