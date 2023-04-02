from re import findall


def count_word(txt):
    """
    Returns a dictionary containing the count of each word in `txt` and the length of each word.

    Parameters:
    txt (str): A string containing words.

    Returns:
    dict: A dictionary containing the count of each word in `txt` and the length of each word.
    """
    return {word: len(word) for word in (findall(r'\w+', txt.lower()))}


text = """
You see, wire telegraph is a kind of a very, very long cat.
You pull his tail in New York and his head is meowing in Los Angeles.
Do you understand this?
And radio operates exactly the same way: you send signals here, they receive them there.
The only difference is that there is no cat.
"""

print(count_word(text))
