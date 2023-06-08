import time


def function_timer(function, *arguments, **kwarguments):
    """
    Measures the elapsed time for executing a function with given arguments and keyword arguments.

    Params:
        function (function): The function to be timed.
        *arguments: Variable length argument list for the function.
        **kwarguments: Arbitrary keyword arguments for the function.

    Returns:
        str: A string representing the elapsed time in seconds.
    """
    measure_start = time.monotonic()
    function(*arguments, **kwarguments)
    measure_end = time.monotonic()
    return f"Elapsed time: {measure_end - measure_start:.6f} seconds"


def main():
    """
    The main entry point of the program.
    """
    print(function_timer(print, "Hello"))
    print(function_timer(zip, [1, 2, 3], [4, 5, 6]))
    print(function_timer("Hi {name}".format, name="Bug"))


if __name__ == '__main__':
    main()
