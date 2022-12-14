"""Returns the distance from origin"""

from typing import Union


def abso(num: Union[int, float]) -> Union[int, float]:
    """Returns the distance from origin

    :param num: Number to check the distance from
    :type num: Union[int, float]
    :return: Distance from `0`
    :rtype: Union[int, float]

    >>> abs(4)
    4
    >>> abs(-3)
    3
    """
    if num < 0:
        return 0 - num
    return num
