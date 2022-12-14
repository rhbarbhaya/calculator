"""Raise a number to the power exponent"""

from typing import Union


def power(num: Union[int, float], exponent: Union[int, float]) -> Union[int, float]:
    """Raise the number to the power

    :param num: The number which acts as the base
    :type num: Union[int, float]
    :param exponent: Raise the number to the power
    :type exponent: Union[int, float]
    :return: Number to power
    :rtype: Union[int, float]

    >>> power(2,3)
    8
    >>> power(5.1, 2.1)
    30.6123993204
    """
    return num**exponent
