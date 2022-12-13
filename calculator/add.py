"""Sums the inputs for the calculator application"""

def add(
    num1: int|float,
    num2: int|float
) -> int|float:
    """Sums and returns the input of two inputs

    :param num1: First input number of the addition method
    :type num1: int or float
    :param num2: Second input number of the addition method
    :type num2: int or float
    :return: Sum of the First and Second number
    :rtype: int or float
    
    >>> add(3, 4)
    7
    >>> add(10.2, 4.2)
    14.4
    """
    return num1 + num2
