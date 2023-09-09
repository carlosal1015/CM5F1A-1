#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial
import sympy as sp


def check_lagrange():
    t = sp.Symbol("t", real=True)
    l_0 = 0.5 * t * (t - 1)
    l_1 = -(t + 1) * (t - 1)
    l_2 = 0.5 * (t + 1) * t
    p_lagrange = (0.5 * l_0 + l_1 - l_2).simplify()
    print(p_lagrange)


plt.rcParams["text.usetex"] = True
plt.rcParams["font.serif"] = ["Computer Modern"]


def plot_interpolation(t: np.array, x: np.array):
    poly = lagrange(t, x)
    # print(poly)
    p = Polynomial(poly.coef[::-1]).coef
    # print(p)
    plt.scatter(t, x, s=10, label="Puntos de control")
    delta = 0.1
    t_new = np.arange(start=-1 - delta, stop=1 + delta, step=0.01)
    plt.plot(
        t_new,
        Polynomial(poly.coef[::-1])(t_new),
        "orange",
        lw=0.45,
        label=f"$p_2(t)={{{p[2]}}}t^2{{{p[1]}}}t+{{{p[0]}}}$",
    )
    plt.grid()
    plt.legend(title="Leyenda", shadow=True, fancybox=True)
    plt.title(f"Polinomio interpolador de Lagrange $p_2(t)$")
    plt.savefig("p6.pdf", transparent=True, bbox_inches="tight")


def plot_basis_lagrange(t: np.array, x: np.array):
    plt.cla()
    delta = 0.1
    t_new = np.arange(start=-1 - delta, stop=1 + delta, step=0.01)
    plt.scatter(t, np.zeros_like(t), s=10)
    plt.plot(
        t_new,
        1 / 2 * t_new**2 - 1 / 2 * t_new,
        lw=0.45,
        label=r"$\ell_{0}(t)=\frac{t^2}{2}-\frac{t}{2}$",
    )
    plt.plot(t_new, 1 - t_new**2, lw=0.45, label=r"$\ell_{1}(t)=1-t^2$")
    plt.plot(
        t_new,
        1 / 2 * t_new**2 + t_new / 2,
        lw=0.45,
        label=r"$\ell_{2}(t)=\frac{t^2}{2}+\frac{t}{2}$",
    )
    plt.grid()
    plt.legend(title="Leyenda", shadow=True, fancybox=True)
    plt.title(f"Funciones base de Lagrange")
    plt.savefig("p6_lagrange.pdf", transparent=True, bbox_inches="tight")


if __name__ == "__main__":
    t = np.array([-1, 0, 1])
    x = np.array([1 / 2, 1, -1])
    check_lagrange()
    plot_interpolation(t=t, x=x)
    plot_basis_lagrange(t=t, x=x)
