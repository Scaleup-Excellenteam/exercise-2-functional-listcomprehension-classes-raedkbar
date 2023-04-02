import time


def timer(f, *args, **kwargs):
    """
    Measures the time taken by a function to execute with the provided arguments.

    Args:
        f (callable): The function to be executed.
        *args: Arbitrary positional arguments to be passed to the function.
        **kwargs: Arbitrary keyword arguments to be passed to the function.

    Returns:
        float: The elapsed time in seconds.
    """
    start = time.monotonic()
    f(*args, **kwargs)
    end = time.monotonic()
    return f"Elapsed time: {end - start:.6f} seconds"


print(timer(print, "Hello"))
print(timer(zip, [1, 2, 3], [4, 5, 6]))
print(timer("Hi {name}".format, name="Bug"))
