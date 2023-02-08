"""
This module is meant to implement functions to solve polynomial equations up to third degree and auxiliary functions that operate on complex numbers.

The functions defined on this module are the following:

imag(z)
real(z)
linear(a, b)
quadratic(a, b, c)
cubic(a, b, c, d)
"""

import cmath as cm
import math as mt


def _imag(z: int | float | complex) -> float:
    """
    Calculate the imaginary part of the input.

    Args:
        z (int | float | complex): Input.

    Returns:
        float: Imaginary part of the input.
    """

    return complex(z).imag


def _real(z: int | float | complex) -> float:
    """
    Calculate the real part of the input.

    Args:
        z (int | float | complex): Input.

    Returns:
        float: Real part of the input.
    """

    return complex(z).real


def _linear(a: int | float, b: int | float) -> tuple[complex]:
    """
    Function to calculate the root of a first degree polynomial equation of the form ax+b=0.

    Args:
        a (int | float): Linear coefficient.
        b (int | float): Constant coefficient.

    Returns:
        tuple[complex]: Tuple with complex roots. Empty tuple if equation is reduced to b = 0.
    """

    if a == 0:
        return ()

    return complex(-b/a),


def _quadratic(a: int | float, b: int | float, c: int | float) -> tuple[complex]:
    """
    Function to calculate the root of a second degree polynomial equation of the form ax^2+bx+c=0.

    Args:
        a (int | float): Quadratic coefficient.
        b (int | float): Linear coefficient.
        c (int | float): Constant coefficient.

    Returns:
        tuple[complex]: Tuple with complex roots. Empty tuple if equation is reduced to c = 0.
    """

    if a == 0:
        return _linear(b, c)

    delta = b**2 - 4*a*c

    x1 = (-b-cm.sqrt(delta))/(2*a) + complex(0, 0)
    x2 = (-b+cm.sqrt(delta))/(2*a) + complex(0, 0)

    return (x1, x2)


def _cubic(a: int | float, b: int | float, c: int | float, d: int | float) -> tuple[complex]:
    """
    Function to calculate the root of a third degree polynomial equation of the form ax^3+bx^2+cx+d=0.

    Args:
        a (int | float): Cubic coefficient.
        b (int | float): Quadratic coefficient.
        c (int | float): Linear coefficient.
        d (int | float): Constant coefficient.

    Returns:
        tuple[complex]: Tuple with complex roots. Empty tuple if equation is reduced to d = 0.
    """

    if a == 0:
        return _quadratic(b, c, d)

    f = (3*c/a - (b**2)/(a**2))/3
    g = (((2*b**3)/(a**3)) - ((9*b*c)/(a**2)) + (27*d/a))/27
    h = ((g**2)/4 + (f**3)/27)

    if f == 0 and g == 0 and h == 0:
        if d/a >= 0:
            x = -(d/a)**(1/3) + complex(0, 0)
        else:
            x = (-d/a)**(1/3) + complex(0, 0)
        return (x, x, x)

    elif _real(h) <= 0:

        i = mt.sqrt(((g**2)/4) - h)
        j = i**(1/3)
        k = mt.acos(-(g/(2*i)))
        L = -j
        M = mt.cos(k/3)
        N = mt.sqrt(3)*mt.sin(k/3)
        P = -b/(3*a)

        x1 = 2*j*mt.cos(k/3) - (b/(3*a)) + complex(0, 0)
        x2 = L * (M + N) + P + complex(0, 0)
        x3 = L * (M - N) + P + complex(0, 0)

        return (x1, x2, x3)

    elif _real(h) > 0:
        R = mt.sqrt(h) - g/2
        if R >= 0:
            S = R**(1/3)
        else:
            S = ((-R)**(1/3)) * -1
        T = -g/2 - mt.sqrt(h)
        if T >= 0:
            U = T**(1/3)
        else:
            U = ((-T)**(1/3)) * -1

        x1 = S + U - (b/(3*a)) + complex(0, 0)
        x2 = -(S + U)/2 - (b/(3*a)) + (S - U)*mt.sqrt(3)*complex(0, 1/2) + complex(0, 0)
        x3 = -(S + U)/2 - (b/(3*a)) - (S - U)*mt.sqrt(3)*complex(0, 1/2) + complex(0, 0)

        return (x1, x2, x3)
