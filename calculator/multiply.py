"""Multiply two numbers for the calculator application"""

def mul(
    num1: int|float,
    num2: int|float
) -> int|float:
    """Returns the multiplication of two numbers

    :param num1: First number in the multiplication script
    :type num1: int or float
    :param num2: Second number for the multiplication script
    :type num2: int or float
    :return: Multiplication of two numbers
    :rtype: int or float
    
    >>> mul(4, 2)
    8
    >>> mul(2.2, 4.2)
    9.24
    """
    return num1 * num2