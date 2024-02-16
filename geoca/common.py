"""The common module contains common functions and classes used by the other modules.
"""

def hello_world():
    """Prints "Hello World!" to the console.
    """
    print("Hello World!")

def random_number():
    """Generate a random number.

    Returns:
        float: A random number.
    """
    import random
    return random.random()