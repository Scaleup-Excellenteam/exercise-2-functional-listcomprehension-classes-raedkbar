import re


def count_word(txt):
    """
    Counts the length of each word in the given text.

    Params:
        txt (str): The text to count the word lengths in.

    Returns:
        dict: A dictionary where the keys are words from the text, and the values are the lengths of the words.
    """
    words = re.findall(r'\w+', txt.lower())  # Extract words from the text
    word_lengths = {}
    for word in words:
        word_lengths[word] = len(word)
    return word_lengths


def main():
    """
    Main function that demonstrates the usage of the count_word function.
    """
    text = """
    You see, wire telegraph is a kind of a very, very long cat.
    You pull his tail in New York and his head is meowing in Los Angeles.
    Do you understand this?
    And radio operates exactly the same way: you send signals here, they receive them there.
    The only difference is that there is no cat.
    """

    print(count_word(text))


if __name__ == '__main__':
    main()
