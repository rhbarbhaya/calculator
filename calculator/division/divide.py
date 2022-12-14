"""Division of two numbers and returns the quotient"""

from typing import Union


def div(num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
    """Division of two numbers for result

    :param num1: Divident
    :type num1: Union[int, float]
    :param num2: Divisor
    :type num2: Union[int, float]
    :raises ZeroDivisionError: Divisor cannot be zero
    :return: Divident divided by the divisor
    :rtype: Union[int, float]

    >>> div(4, 4)
    1
    >>> div(8.2, 2)
    4.1
    """
    if num2 == 0:
        raise ZeroDivisionError("Divisor cannot be Zero")
    return num2 / num1
