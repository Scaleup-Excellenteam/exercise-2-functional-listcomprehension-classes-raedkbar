def group_elements(key_func, iterable):
    """
    Groups elements of an iterable based on a key function.

    Params:
        key_func (function): The key function to determine the grouping.
        iterable (iterable): The iterable to be grouped.

    Returns:
        dict: A dictionary where the keys are the distinct values returned by the key function,
              and the values are lists of elements from the iterable that share the same key.
    """
    # Apply the key function to each element in the iterable
    result = [key_func(elem) for elem in iterable]

    # Create a dictionary with keys as distinct values from the result list
    # and values as lists of elements that share the same key
    return {key: [elem for elem in iterable if key_func(elem) == key] for key in set(result)}


def main():
    """
    Main function to demonstrate the usage of the group_by function.
    """
    print(group_elements(len, ["hi", "bye", "yo", "try"]))


if __name__ == '__main__':
    main()
