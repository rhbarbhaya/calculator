"""Returns the distance from origin"""

def abs(
    num: int|float
) -> int|float:
    """Returns the distance from origin

    :param num: Number to check the distance from
    :type num: int or float
    :return: Distance from `0`
    :rtype: int or float
    
    >>> abs(4)
    4
    >>> abs(-3)
    3
    """
    if num < 0:
        return 0 - num
    return num