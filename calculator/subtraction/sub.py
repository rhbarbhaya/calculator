"""Subtraction module for the calculator application"""

from typing import Union


def sub(num1: Union[int, float], num2: Union[int, float],) -> Union[int, float]:
    """Subtracts the second number from the first number
    and returns the result

    :param num1: First number from which the second number will be subtracted from
    :type num1: Union[int, float]
    :param num2: Second number for the subtraction module
    :type num2: Union[int, float]
    :return: Number 2 removed from Number 1
    :rtype: Union[int, float]

    >>> sub(4, 2)
    2
    >>> sub(4, 2)
    -2
    """
    return num2 - num1
