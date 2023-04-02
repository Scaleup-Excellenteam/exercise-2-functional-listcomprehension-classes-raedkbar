from PIL import Image
import os.path


def decipher(img):
    """
    This function takes an image and deciphers a hidden message within it.

    Parameters:
    image (PIL.Image.Image): An image object containing a hidden message.

    Returns:
    str: The deciphered message string.
    """
    message = ""
    pixel = img.load()
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            if pixel[x, y] == 1:
                message += chr(y)

    return message


if os.path.exists('resources/code.png'):
    with Image.open('resources/code.png') as image:
        print(decipher(image))
else:
    print("Image file not found.")
