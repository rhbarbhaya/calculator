"""Raise a number to the power exponent"""

def power(
    num: int | float,
    exponent: int | float
) -> int | float:
    """Raise the number to the power

    :param num: The number which acts as the base
    :type num: int or float
    :param exponent: Raise the number to the power
    :type exponent: int or float
    :return: Number to power
    :rtype: int or float
    
    >>> power(2,3)
    8
    >>> power(5.1, 2.1)
    30.6123993204
    """
    return num ** exponent