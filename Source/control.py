import polynomial as pl
import math as mt
from math import pi
from cmath import phase
import sig_fig as sf
import matplotlib.pyplot as plt


(_a1, _a2, _b1, _b2, _c1, _c2, _d1, _d2) = (0, 0, 0, 0, 0, 0, 0, 0)

_freqs = []
_poles = []
_zeros = []


def _H(p: int | float | complex) -> complex:
    """
    Calculates the transfer function at a given p value.

    Args:
        p (int | float | complex): Laplace variable.

    Returns:
        complex: Transfer function calculated on the given p value.
    """

    numerator = 0
    if (_a1, _b1, _c1) == (0, 0, 0):
        numerator = _d1
    elif (_a1, _b1) == (0, 0):
        numerator = _c1
    elif _a1 == 0:
        numerator = _b1
    else:
        numerator = _a1

    denominator = 0
    if (_a2, _b2, _c2) == (0, 0, 0):
        denominator = _d2
    elif (_a2, _b2) == (0, 0):
        denominator = _c2
    elif _a2 == 0:
        denominator = _b2
    else:
        denominator = _a2

    for _p in _zeros:
        numerator = numerator*(p - _p)

    for _p in _poles:
        denominator = denominator*(p - _p)

    return numerator/denominator


def H(f: int | float) -> None:
    """
    Calculates the transfer function at a given real frequency and prints the magnitude in dB and phase in degrees.

    Args:
        f (int | float): Input frequency.
    """

    z = _H(2*pi*f)
    phi = phase(z)*180/pi

    print(43*"-")
    try:
        G = 20*mt.log10(abs(z))
        print(sf._round_fix(G, unit="dB"))
    except:
        print("-inf dB")

    if abs(phi) < 1:
        print(sf._round_fix(phi, unit="deg"))
    else:
        print(sf._round_fix(phi, unit="deg"))
    print(43*"-")


def _is_equal(z1: int | float | complex, z2: int | float | complex, n: int = 5) -> bool:
    """
    Verify if two complex numbers are equal up to a given tolerance. Returns true if both real and imaginary parts are withing tolerance and/or both magnitude and phase are withing tolerance. To check if any 2 numbers are withing tolerance, truncates both values up to n significant figures and check if they are equal.

    Args:
        z1 (int | float | complex): First complex number.
        z2 (int | float | complex): Second complex number.
        n (int, optional): Significant figures for tolerance checking. Defaults to 5.

    Returns:
        bool: If the numbers are equal or not.
    """

    a1 = pl._real(z1)
    if a1 != 0:
        a1_exp = mt.floor(mt.log10(abs(a1)))
        a1_norm = a1/(10**a1_exp)
        a1_norm = round(a1_norm, n-1)
        a1 = a1_norm*(10**a1_exp)

    b1 = pl._imag(z1)
    if b1 != 0:
        b1_exp = mt.floor(mt.log10(abs(b1)))
        b1_norm = b1/(10**b1_exp)
        b1_norm = round(b1_norm, n-1)
        b1 = b1_norm*(10**b1_exp)

    r1 = abs(z1)
    if r1 != 0:
        r1_exp = mt.floor(mt.log10(abs(r1)))
        r1_norm = r1/(10**r1_exp)
        r1_norm = round(r1_norm, n-1)
        r1 = r1_norm*(10**r1_exp)

    phi1 = phase(z1)
    if phi1 != 0:
        phi1_exp = mt.floor(mt.log10(abs(phi1)))
        phi1_norm = phi1/(10**phi1_exp)
        phi1_norm = round(phi1_norm, n-1)
        phi1 = phi1_norm*(10**phi1_exp)

    a2 = pl._real(z2)
    if a2 != 0:
        a2_exp = mt.floor(mt.log10(abs(a2)))
        a2_norm = a2/(10**a2_exp)
        a2_norm = round(a2_norm, n-1)
        a2 = a2_norm*(10**a2_exp)

    b2 = pl._imag(z2)
    if b2 != 0:
        b2_exp = mt.floor(mt.log10(abs(b2)))
        b2_norm = b2/(10**b2_exp)
        b2_norm = round(b2_norm, n-1)
        b2 = b2_norm*(10**b2_exp)

    r2 = abs(z2)
    if r2 != 0:
        r2_exp = mt.floor(mt.log10(abs(r2)))
        r2_norm = r2/(10**r2_exp)
        r2_norm = round(r2_norm, n-1)
        r2 = r2_norm*(10**r2_exp)

    phi2 = phase(z2)
    if phi2 != 0:
        phi2_exp = mt.floor(mt.log10(abs(phi2)))
        phi2_norm = phi2/(10**phi2_exp)
        phi2_norm = round(phi2_norm, n-1)
        phi2 = phi2_norm*(10**phi2_exp)

    return (a1, b1) == (a2, b2) or (r1, phi1) == (r2, phi2)


def coeffs() -> None:
    """
    Function that changes the global variables representing the linear system in question.
    """

    global _a1, _b1, _c1, _d1
    global _a2, _b2, _c2, _d2
    global _freqs
    global _poles, _zeros

    print("Enter numerator coefficients")
    print("ap^3+bp^2+cp+d")
    _a1 = float(input("a = "))
    _b1 = float(input("b = "))
    _c1 = float(input("c = "))
    _d1 = float(input("d = "))

    print("\nEnter denominator coefficients")
    print("ap^3+bp^2+cp+d")
    _a2 = float(input("a = "))
    _b2 = float(input("b = "))
    _c2 = float(input("c = "))
    _d2 = float(input("d = "))

    _zeros = list(pl._cubic(_a1, _b1, _c1, _d1))
    _poles = list(pl._cubic(_a2, _b2, _c2, _d2))

    for p in _poles[:]:
        for z in _zeros[:]:
            if _is_equal(p, z):
                _poles.remove(p)
                _zeros.remove(z)

    _freqs = []

    for p in _poles + _zeros:
        f = abs(p/(2*pi))
        _freqs.append(f)

    _freqs.sort()


def pole_values() -> None:
    """
    Function that prints all poles and zeros and their corresponding frequencies, damping coefficients and quality factors.
    """

    print(43*"-")
    if len(_poles) == 0:
        print("No poles")
    else:
        print("Poles:")
        for i in range(len(_poles)):
            print("\np"+str(i+1)+" = "+sf._complex_round_fix(_poles[i]))
            print("f"+str(i+1)+" = "+sf._round_eng(abs(_poles[i]/(2*pi)), unit="Hz"))
            print("m"+str(i+1)+" = "+sf._round_fix(-mt.cos(phase(_poles[i]))))
            print("Q"+str(i+1)+" = "+sf._round_fix(-1/(2*mt.cos(phase(_poles[i])))))

    print(43*"-")
    if len(_zeros) == 0:
        print("No zeros")
    else:
        print("Zeros:")
        for i in range(len(_zeros)):
            print("\nz"+str(i+1)+" = "+sf._complex_round_fix(_zeros[i]))
            print("f"+str(i+1)+" = "+sf._round_eng(abs(_zeros[i]/(2*pi)), unit="Hz"))
            print("m"+str(i+1)+" = "+sf._round_fix(-mt.cos(phase(_zeros[i]))))
            print("Q"+str(i+1)+" = "+sf._round_fix(-1/(2*mt.cos(phase(_zeros[i])))))

    print(43*"-")
    print("Corner frequencies:\n")
    for i in range(len(_freqs)):
        print("f"+str(i+1)+" = "+sf._round_eng(_freqs[i], unit="Hz"))


def root_locust_plot() -> None:
    """
    Function that plots all poles in orange and zeros in blue on the complex plane.
    """

    xmax = 0
    ymax = 0

    if len(_poles) != 0:
        x_poles = [pl._real(p) for p in _poles]
        y_poles = [pl._imag(p) for p in _poles]
        xmax = max([xmax]+[abs(x) for x in x_poles])
        ymax = max([ymax]+[abs(y) for y in y_poles])
        plt.scatter(x_poles, y_poles, color="orange")

    if len(_zeros) != 0:
        x_zeros = [pl._real(p) for p in _zeros]
        y_zeros = [pl._imag(p) for p in _zeros]
        xmax = max([xmax]+[abs(x) for x in x_zeros])
        ymax = max([ymax]+[abs(y) for y in y_zeros])
        plt.scatter(x_zeros, y_zeros, color="blue")

    if xmax == 0:
        xmax = 1
    else:
        xmax *= 1.1

    if ymax == 0:
        ymax = 1
    else:
        ymax *= 1.1

    plt.axis((-xmax, xmax, -ymax, ymax))
    plt.show()


def mag_plot(fmin: int | float = 0, fmax: int | float = 0) -> None:
    """
    Function that plots the gain Bode diagram. If not specified, the frequency range goes from 2 decades lower than the minimal corner frequency (excluding frequency zero) up to 2 decades higher than the maximal corner frequency. The y axis displays the gain in decibels and the x axis displays the log of frequency.

    Args:
        fmin (int | float, optional): Frequency sweep start. Defaults to 0.
        fmax (int | float, optional): Frequency sweep end. Defaults to 0.
    """

    N = 500
    while N > 0:
        try:
            if fmin <= 0 or fmax <= 0 or fmax <= fmin:
                _freqs = (f for f in _freqs if f != 0)
                xmin = mt.log10(min(_freqs)/100)

                _freqs = (f for f in _freqs if f != 0)
                xmax = mt.log10(max(_freqs)*100)
            else:
                xmin = mt.log10(fmin)
                xmax = mt.log10(fmax)

            delta_dec = xmax - xmin

            x_list = [delta_dec*i/(N-1) + xmin for i in range(N)]
            p_list = (2*pi*(10**x) for x in x_list)

            mag_list = []

            for p in p_list:
                try:
                    mag_list.append(20*mt.log10(abs(_H(p))))
                except:
                    mag_list.append(20*mt.log10(abs(_H(p+1e-10))))

            plt.plot(x_list, mag_list, color="blue")
            break
        except:
            N -= 10
    else:
        print("Unable to allocate memory")
        return

    plt.show()


def phase_plot(fmin: int | float = 0, fmax: int | float = 0) -> None:
    """
    Function that plots phase Bode diagram. The frequency range goes from 2 decades lower than the minimal corner frequency (excluding frequency zero) up to 2 decades higher than the maximal corner frequency. The y axis displays the phase in degrees and the x axis displays the log of frequency.

    Args:
        fmin (int | float, optional): Frequency sweep start. Defaults to 0.
        fmax (int | float, optional): Frequency sweep end. Defaults to 0.
    """

    N = 500

    while N > 0:
        try:
            if fmin <= 0 or fmax <= 0 or fmax <= fmin:
                _freqs = (f for f in _freqs if f != 0)
                xmin = mt.log10(min(_freqs)/100)

                _freqs = (f for f in _freqs if f != 0)
                xmax = mt.log10(max(_freqs)*100)
            else:
                xmin = mt.log10(fmin)
                xmax = mt.log10(fmax)

            delta_dec = xmax - xmin

            x_list = [delta_dec*i/(N-1) + xmin for i in range(N)]
            p_list = (2*pi*(10**x) for x in x_list)

            phase_list = [phase(_H(p))*180/pi for p in p_list]

            for i in range(1, N):
                delta = phase_list[i] - phase_list[i-1]
                if abs(delta) > 150:
                    phase_list[i] -= mt.copysign(mt.ceil(abs(delta)/180)*180, delta)

            plt.plot(x_list, phase_list, color="blue")
            break
        except:
            N -= 10
    else:
        print("Unable to allocate memory")
        return

    plt.show()


def nyquist_plot(fmin: int | float = 0, fmax: int | float = 0) -> None:
    """
    Function that plots the Nyquist plot. The frequency range goes from 2 decades lower than the minimal corner frequency (excluding frequency zero) up to 2 decades higher than the maximal corner frequency. The y axis displays the imaginary part and the x axis displays the real part. Also plots the point -1+0j to faccilitate stability checking.

    Args:
        fmin (int | float, optional): Frequency sweep start. Defaults to 0.
        fmax (int | float, optional): Frequency sweep end. Defaults to 0.
    """

    N = 500

    while N > 0:
        try:
            if fmin <= 0 or fmax <= 0 or fmax <= fmin:
                _freqs = (f for f in _freqs if f != 0)
                xmin = mt.log10(min(_freqs)/100)

                _freqs = (f for f in _freqs if f != 0)
                xmax = mt.log10(max(_freqs)*100)
            else:
                xmin = mt.log10(fmin)
                xmax = mt.log10(fmax)

            delta_dec = xmax - xmin

            x_list = [delta_dec*i/(N-1) + xmin for i in range(N)]
            p_list = (2*pi*(10**x) for x in x_list)

            a_list = []
            b_list = []

            for p in p_list:
                a_list.append(pl._real(_H(p)))
                b_list.append(pl._imag(_H(p)))

            plt.scatter(-1, 0, color="black")
            plt.plot(a_list, b_list, color="blue")
            break
        except:
            N -= 10
    else:
        print("Unable to allocate memory")
        return

    plt.show()


def nichols_plot(fmin: int | float = 0, fmax: int | float = 0) -> None:
    """
    Function that plots the Nichols plot. The frequency range goes from 2 decades lower than the minimal corner frequency (excluding frequency zero) up to 2 decades higher than the maximal corner frequency. The y axis displays the gain in decibels and the x axis displays phase in degrees. Also plots the point (0 dB, -180 deg) to faccilitate stability checking.

    Args:
        fmin (int | float, optional): Frequency sweep start. Defaults to 0.
        fmax (int | float, optional): Frequency sweep end. Defaults to 0.
    """

    N = 500

    while N > 0:
        try:
            if fmin <= 0 or fmax <= 0 or fmax <= fmin:
                _freqs = (f for f in _freqs if f != 0)
                xmin = mt.log10(min(_freqs)/100)

                _freqs = (f for f in _freqs if f != 0)
                xmax = mt.log10(max(_freqs)*100)
            else:
                xmin = mt.log10(fmin)
                xmax = mt.log10(fmax)

            delta_dec = xmax - xmin

            x_list = [delta_dec*i/(N-1) + xmin for i in range(N)]
            p_list = (2*pi*(10**x) for x in x_list)

            phase_list = []
            mag_list = []

            for p in p_list:
                try:
                    mag_list.append(20*mt.log10(abs(_H(p))))
                    phase_list.append(phase(_H(p))*180/pi)
                except:
                    mag_list.append(20*mt.log10(abs(_H(p+1e-10))))
                    phase_list.append(phase(_H(p+1e-10))*180/pi)

            for i in range(1, N):
                delta = phase_list[i] - phase_list[i-1]
                if abs(delta) > 150:
                    phase_list[i] -= mt.copysign(mt.ceil(abs(delta)/180)*180, delta)

            plt.scatter(-180, 0, color="black")
            plt.plot(phase_list, mag_list, color="blue")
            break
        except:
            N -= 10
    else:
        print("Unable to allocate memory")
        return

    plt.show()


def stab(tol: float = 0.0001, iter: int = 500) -> None:
    """
    Function that uses bissection method to calculate and print phase and gain margins. Meant to be used on low-pass filters.

    Args:
        tol (float, optional): Percentual tolerance for bissection method. Defaults to 0.0001.
        iter (int, optional): Maximum number of iterations. Defaults to 500.
    """

    fmin = min(_freqs)/100
    if fmin == 0:
        fmin = 1
    fmax = 100*fmin
    fmid = mt.sqrt(fmin*fmax)

    Gmin = abs(_H(2*pi*fmin))
    Gmid = abs(_H(2*pi*fmid))
    Gmax = abs(_H(2*pi*fmax))

    counter = 0
    while Gmin > 1 and Gmax > 1:
        if counter >= iter:
            print("Not able to find margins")
            return

        fmin *= 10
        fmax *= 10
        fmid = mt.sqrt(fmin*fmax)

        Gmin = abs(_H(2*pi*fmin))
        Gmid = abs(_H(2*pi*fmid))
        Gmax = abs(_H(2*pi*fmax))

        counter += 1

    counter = 0
    while Gmin < 1 and Gmax < 1:
        if counter >= iter:
            print("Not able to find margins")
            return

        fmin *= 0.1
        fmax *= 0.1
        fmid = mt.sqrt(fmin*fmax)

        Gmin = abs(_H(2*pi*fmin))
        Gmid = abs(_H(2*pi*fmid))
        Gmax = abs(_H(2*pi*fmax))

        counter += 1

    counter = 0
    while abs(Gmin - 1) > tol:
        if counter >= iter:
            print("Not able to find margins")
            return

        fmid = mt.sqrt(fmin*fmax)

        Gmin = abs(_H(2*pi*fmin))
        Gmid = abs(_H(2*pi*fmid))
        Gmax = abs(_H(2*pi*fmax))

        if Gmid > 1 and Gmax < 1:
            fmin = fmid
        elif Gmin > 1 and Gmid < 1:
            fmax = fmid
        elif Gmid < 1 and Gmax > 1:
            fmin = fmid
        elif Gmin < 1 and Gmid > 1:
            fmax = fmid
        counter += 1

    f_0dB = fmin

    fmin = min(_freqs)/100
    if fmin == 0:
        fmin = 1
    fmax = 100*fmin
    fmid = mt.sqrt(fmin*fmax)

    Pmin = phase(_H(2*pi*fmin))
    if Pmin >= 0:
        Pmin -= 2*pi

    Pmid = phase(_H(2*pi*fmid))
    if Pmid >= 0:
        Pmid -= 2*pi

    Pmax = phase(_H(2*pi*fmax))
    if Pmax >= 0:
        Pmax -= 2*pi

    counter = 0
    while Pmin > -pi and Pmax > -pi:
        if counter >= iter:
            print("Not able to find margins")
            return

        fmin *= 10
        fmax *= 10
        fmid = mt.sqrt(fmin*fmax)

        Pmin = phase(_H(2*pi*fmin))
        if Pmin >= 0:
            Pmin -= 2*pi

        Pmid = phase(_H(2*pi*fmid))
        if Pmid >= 0:
            Pmid -= 2*pi

        Pmax = phase(_H(2*pi*fmax))
        if Pmax >= 0:
            Pmax -= 2*pi

        counter += 1

    counter = 0
    while Pmin < -pi and Pmax < -pi:
        if counter >= iter:
            print("Not able to find margins")
            return

        fmin *= 0.1
        fmax *= 0.1
        fmid = mt.sqrt(fmin*fmax)

        Pmin = phase(_H(2*pi*fmin))
        if Pmin >= 0:
            Pmin -= 2*pi

        Pmid = phase(_H(2*pi*fmid))
        if Pmid >= 0:
            Pmid -= 2*pi

        Pmax = phase(_H(2*pi*fmax))
        if Pmax >= 0:
            Pmax -= 2*pi

        counter += 1

    counter = 0
    while abs(Pmin/pi + 1) > tol:
        if counter >= iter:
            print("Not able to find margins")
            return

        fmid = mt.sqrt(fmin*fmax)

        Pmin = phase(_H(2*pi*fmin))
        if Pmin >= 0:
            Pmin -= 2*pi

        Pmid = phase(_H(2*pi*fmid))
        if Pmid >= 0:
            Pmid -= 2*pi

        Pmax = phase(_H(2*pi*fmax))
        if Pmax >= 0:
            Pmax -= 2*pi

        if Pmid > -pi and Pmax < -pi:
            fmin = fmid
        elif Pmin > -pi and Pmid < -pi:
            fmax = fmid
        elif Pmid < -pi and Pmax > -pi:
            fmin = fmid
        elif Pmin < -pi and Pmid > -pi:
            fmax = fmid
        counter += 1

    f_pi = fmin

    Pt = phase(_H(2*pi*f_0dB))
    if Pt >= 0:
        Pt -= 2*pi
    pm = 180 + Pt*180/pi

    gm = -20*mt.log10(abs(_H(2*pi*f_pi)))

    print(43*"-")
    if abs(pm) < 1:
        print("Phase margin: "+sf._round_sci(pm, unit="deg"))
    else:
        print("Phase margin: "+sf._round_eng(pm, unit="deg"))

    print("Gain margin: "+sf._round_eng(gm, unit="dB"))

    print("\nPhase crossover: "+sf._round_eng(f_pi, unit="Hz"))
    print("Gain crossover: "+sf._round_eng(f_0dB, unit="Hz"))
    print(43*"-")


coeffs()
