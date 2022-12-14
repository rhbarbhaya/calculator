from calculator import (
    add,
    sub,
    mul,
    div,
    abso,
    power,
)
import pytest


@pytest.mark.parametrize(
    'num1, num2, res', [
        (2, 3, 5),
        (-1, -3, -4),
        (4.2, 8.1, 12.3),
        (3, -5, -2)
    ]
)
def test_add(num1, num2, res):
    assert add(num1, num2) == pytest.approx(res)


@pytest.mark.parametrize(
    'num1, num2, res', [
        (2, 3, 1),
        (-1, -3, -2),
        (4.2, 8.1, 3.9),
        (3, -5, -8)
    ]
)
def test_sub(num1, num2, res):
    assert sub(num1, num2) == pytest.approx(res)


@pytest.mark.xfail(raises=ZeroDivisionError)
def test_div2():
    div(2, 0)
    
@pytest.mark.parametrize(
    'num1, num2, res',[
        (2, 3, 1.5),
        (-1, -3, 3),
        (4.2, 8.1, 1.92857),
        (3, 1, 0.3333333)
    ]
)
def test_div(num1, num2, res):
    assert div(num1, num2) == pytest.approx(res)

@pytest.mark.parametrize(
    'num1, num2, res',[
        (2, 3, 6),
        (-1, -3, 3),
        (4.2, 8.1, 34.02),
        (3, -5, -15)
    ]
)
def test_mul(num1, num2, res):
    assert mul(num1, num2) == pytest.approx(res)

@pytest.mark.parametrize(
    'num, res',[
        (2, 2),
        (-1, 1),
        (4.2, 4.2),
        (-5, 5),
        (0, 0)
    ]
)
def test_abs(num, res):
    assert abso(num) == pytest.approx(res)

@pytest.mark.parametrize(
    'num1, num2, res',[
        (2, 3, 8),
        (-1, -3, -1),
        (4.2, 8.1, 111768.4561834),
        (3, -5, 0.004115226)
    ]
)
def test_power(num1, num2, res):
    assert power(num1, num2) == pytest.approx(res)