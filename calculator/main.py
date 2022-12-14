"""Entry point script"""

from calculator.addition.add import add
from calculator.absolute.absolute import abso
from calculator.subtraction.sub import sub
from calculator.multiplication.multiply import mul
from calculator.division.divide import div
from calculator.power.power import power


def main() -> None:
    """Entry point for the script"""
    print(f"Absolute of -3.2  :: {abso(-3.2)}")
    print(f"Addition of 3 & 7 :: {add(3, 7)}")
    print(f"Division of 7 by 2 :: {div(7, 2)}")
    print(f"Multiplication of 5.9 & 4.2 :: {mul(5.9, 4.2)}")
    print(f"Subtraction of 90 with 42 :: {sub(42, 90)}")
    print(f"Exponent of 2 to 8 :: {power(2, 8)}")


if __name__ == "__main__":
    main()