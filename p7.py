#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial
import sympy as sp


def check_lagrange():
    t = sp.Symbol("t", real=True)
    l_0 = -(t**3) + 7 / 2 * t**2 - 7 / 2 * t + 1
    l_1 = 8 / 3 * t**3 - 8 * t**2 + 16 / 3 * t
    l_2 = -2 * t**3 + 5 * t**2 - 2 * t
    l_3 = 1 / 3 * t**3 - 1 / 2 * t**2 + 1 / 6 * t
    p_lagrange = (1 * l_0 + 2 * l_1 + 3 / 2 * l_2 - l_3).simplify()
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
    t_new = np.arange(start=0 - delta, stop=2 + delta, step=0.01)
    plt.plot(
        t_new,
        Polynomial(poly.coef[::-1])(t_new),
        "orange",
        lw=0.45,
        label=f"$p_3(t)={{{np.round(p[3])}}}t^3{{{p[2]}}}t^2+{{{np.round(p[1])}}}t+{{{p[0]}}}$",
    )
    plt.grid()
    plt.legend(title="Leyenda", shadow=True, fancybox=True)
    plt.title(f"Polinomio interpolador de Lagrange $p_3(t)$")
    plt.savefig("p7.pdf", transparent=True, bbox_inches="tight")


def plot_basis_lagrange(t: np.array, x: np.array):
    plt.cla()
    delta = 0.1
    t_new = np.arange(start=0 - delta, stop=2 + delta, step=0.01)
    plt.scatter(t, np.zeros_like(t), s=10)
    plt.plot(
        t_new,
        -(t_new**3) + 7 / 2 * t_new**2 - 7 / 2 * t_new + 1,
        lw=0.45,
        label=r"$\ell_{0}(t)=-t^3+\frac{7}{2}t^2-\frac{7}{2}t+1$",
    )
    plt.plot(
        t_new,
        8 / 3 * t_new**3 - 8 * t_new**2 + 16 / 3 * t_new,
        lw=0.45,
        label=r"$\ell_{1}(t)=\frac{8}{3}t^3-8t^2+\frac{16}{3}t$",
    )
    plt.plot(
        t_new,
        -2 * t_new**3 + 5 * t_new**2 - 2 * t_new,
        lw=0.45,
        label=r"$\ell_{2}(t)=-2t^3+5t^2-2t$",
    )
    plt.plot(
        t_new,
        1 / 3 * t_new**3 - 1 / 2 * t_new**2 + 1 / 6 * t_new,
        lw=0.45,
        label=r"$\ell_{3}(t)=\frac{1}{3}t^3-\frac{1}{2}t^2+\frac{1}{6}t$",
    )
    plt.grid()
    plt.legend(title="Leyenda", shadow=True, fancybox=True)
    plt.title(f"Funciones base de Lagrange")
    plt.savefig("p7_lagrange.pdf", transparent=True, bbox_inches="tight")


if __name__ == "__main__":
    t = np.array([0, 1 / 2, 1, 2])
    x = np.array([1, 2, 3 / 2, -1])
    check_lagrange()
    plot_interpolation(t=t, x=x)
    plot_basis_lagrange(t=t, x=x)
