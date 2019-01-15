from PIL import Image, ImageFilter, ImageDraw
import numpy as np

def pixelate(image, pixel_x, pixel_y):

    width, height = image.size
    pixels = np.array(image)

    for i in range(height):
        for j in range(width):

            if j % pixel_x == 0:
                if i % pixel_y == 0:
                    color = pixels[i][j]
                else:
                    color = pixels[i - 1][j]
            pixels[i][j] = color

    return Image.fromarray(pixels, "RGB")

try:
    image_path = input("Enter image path: ")

    im = Image.open(image_path)

    x_dimension = int(input("Enter the pixel width: "))
    y_dimension = int(input("Enter the pixel height: "))

    pixelated = pixelate(im, x_dimension, y_dimension)
    pixelated.show()

except IOError:
    print("\nIOError - ", "Given file could not be found or opened")
except:
    print("An unknown error occured")
