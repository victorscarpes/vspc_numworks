def __jury_aux(coeffs: tuple, N: int) -> tuple:
    """
    Auxiliary funtion to calculate the next line in the jury table from the current one.

    Args:
        coeffs (tuple): Tuple containing the current line of the jury table.

    Returns:
        tuple: Tuple  containing the next line of the jury table.
    """

    N: int = len(coeffs)

    if N <= 0:
        return ()

    a: list = list(coeffs)
    b: list = [a[0]*a[k] - a[N]*a[N-k] for k in range(N)]

    return tuple(b)


def jury_test(*coeffs):
    a: list = list(coeffs)
    N: int = len(coeffs) - 1

    if sum(a) <= 0:
        return False

    if sum(an * (-1) ** (N + n) for n, an in enumerate(a)) <= 0:
        return False

    if abs(a[0]) >= abs(a[-1]):
        return False

    while N > 2:
        b: tuple = __jury_aux(a, N)
        N -= 1

        if abs(b[0]) <= abs(b[-1]):
            return False

    return True


print(jury_test(-0.02916, 0.2511, 0.522, -1.12, -0.6, 1))
