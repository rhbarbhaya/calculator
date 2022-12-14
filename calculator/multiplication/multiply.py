"""Multiply two numbers for the calculator application"""

from typing import Union


def mul(num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
    """Returns the multiplication of two numbers

    :param num1: First number in the multiplication script
    :type num1: Union[int, float]
    :param num2: Second number for the multiplication script
    :type num2: Union[int, float]
    :return: Multiplication of two numbers
    :rtype: Union[int, float]

    >>> mul(4, 2)
    8
    >>> mul(2.2, 4.2)
    9.24
    """
    return num1 * num2
