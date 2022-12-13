"""Division of two numbers and returns the quotient"""

def div(
    num1: int | float,
    num2: int | float
) -> int | float:
    """Division of two numbers for result

    :param num1: Divident
    :type num1: int or float
    :param num2: Divisor
    :type num2: int or float
    :raises ZeroDivisionError: Divisor cannot be zero
    :return: Divident divided by the divisor
    :rtype: int or float
    
    >>> div(4, 4)
    1
    >>> div(8.2, 2)
    4.1
    """
    if num1 == 0:
        raise ZeroDivisionError("Divisor cannot be Zero")
    return num2 / num1
