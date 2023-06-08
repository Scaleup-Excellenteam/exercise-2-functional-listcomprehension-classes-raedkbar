from PIL import Image
import os.path


def text_extract(image):
    """
    Extracts a secret message hidden in the image.

    Params:
        img (PIL.Image.Image): The image object to be extracted.

    Returns:
        str: The message.
    """

    pixels = image.load()
    message = ''.join(chr(y) for x in range(image.width) for y in range(image.height) if pixels[x, y] == 1)

    return message


def main():
    """
    Main function that loads an image and extracts the hidden message.

    Prints the extracted message or an error message if the image file is not found.
    """
    if os.path.exists('resources/code.png'):
        with Image.open('resources/code.png') as image:
            print(text_extract(image))
    else:
        print("Image file not found.")


if __name__ == '__main__':
    main()
