"""Subtraction module for the calculator application"""

def sub(
    num1: int|float,
    num2: int|float,
) -> int|float:
    """Subtracts the second number from the first number
    and returns the result

    :param num1: First number from which the second number will be subtracted from
    :type num1: int or float
    :param num2: Second number for the subtraction module
    :type num2: int or float
    :return: Number 2 removed from Number 1
    :rtype: int or float
    
    >>> sub(4, 2)
    2
    >>> sub(4, 2)
    -2
    """
    return num2 - num1
