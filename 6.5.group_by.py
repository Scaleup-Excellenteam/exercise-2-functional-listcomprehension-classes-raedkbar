def group_by(f, iterable):
    """
    Groups the elements in the iterable according to the key function f.
    The key function takes each element and returns a key for it,
    and the elements are then grouped by these keys.

    Args:
    - f: A function that takes an element and returns a key.
    - iterable: An iterable object.

    Returns:
    - A dictionary whose keys are the keys returned by the function f and
    whose values are the list of elements in iterable that have the same key.
    """
    result = [f(elem) for elem in iterable]
    return {key: [elem for elem in iterable if f(elem) == key] for key in set(result)}


print(group_by(len, ["hi", "bye", "yo", "try"]))
