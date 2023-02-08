from matplotlib.pyplot import *
from math import *

g = 9.81


def _x(t, v_0, alpha):
    return v_0*cos(alpha)*t


def _y(t, v_0, alpha, h_0):
    return -0.5*g*t**2+v_0*sin(alpha)*t+h_0


def _vx(v_0, alpha):
    return v_0*cos(alpha)


def _vy(t, v_0, alpha):
    return -g*t+v_0*sin(alpha)


def _t_max(v_0, alpha, h_0):
    return (v_0*sin(alpha)+sqrt((v_0**2)*(sin(alpha)**2)+2*g*h_0))/g


def simulation(v_0=15, alpha=pi/4, h_0=2):
    tMax = _t_max(v_0, alpha, h_0)
    accuracy = 1/10**(floor(log10(tMax))-1)
    T_MAX = floor(tMax*accuracy)+1
    X = [_x(t/accuracy, v_0, alpha) for t in range(T_MAX)]
    Y = [_y(t/accuracy, v_0, alpha, h_0) for t in range(T_MAX)]
    VX = [_vx(v_0, alpha) for t in range(T_MAX)]
    VY = [_vy(t/accuracy, v_0, alpha) for t in range(T_MAX)]
    for i in range(T_MAX):
        arrow(X[i], Y[i], VX[i]/accuracy, VY[i]/accuracy)
    grid()
    show()
