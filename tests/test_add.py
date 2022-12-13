from calculator import add
import pytest

@pytest.mark.parametrize(
    'num1, num2, res',[
        (1, 2, 3),
        (5, 9, 14),
        (-1, -2, -3),
        (0, 7, 7),
        (10.5, 4.4, 14.9)
    ]
)
def test_add(num1: int|float, num2: int|float, res: int|float):
    assert add(num1, num2) == res
