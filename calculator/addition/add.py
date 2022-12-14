"""Sums the inputs for the calculator application"""
from typing import Union


def add(num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
    """Sums and returns the input of two inputs

    :param num1: First input number of the addition method
    :type num1: Union[int, float]
    :param num2: Second input number of the addition method
    :type num2: Union[int, float]
    :return: Sum of the First and Second number
    :rtype: Union[int, float]

    >>> add(3, 4)
    7
    >>> add(10.2, 4.2)
    14.4
    """
    return num1 + num2
