#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial

plt.rcParams["text.usetex"] = True
plt.rcParams["font.serif"] = ["Computer Modern"]

numbers = (5, 8, 10)


def plot_lagrange(numbers):
    for number in numbers:
        x = np.linspace(start=-5, stop=5, num=number)
        delta = 0.5
        t = np.linspace(start=-5 - delta, stop=5 + delta, num=300)
        y = 1 / (1 + x**2)
        y_new = 1 / (1 + t**2)
        poly = lagrange(x, y)
        print(f"P_{number}:\n{poly}")
        p = Polynomial(poly.coef[::-1]).coef
        delta = 0.1
        x_new = np.arange(start=-5 - delta, stop=5 + delta, step=0.01)
        plt.plot(x_new, Polynomial(poly.coef[::-1])(x_new), 'orange',
                 lw=0.45, label=f"$P_{{{number-1}}}(t)$")
        plt.scatter(x, y, s=10, label='Puntos de control')
        plt.plot(t, y_new, lw=0.45, label=r"$f(t)=\frac{1}{1+t^2}$")
        # plt.plot(x, y)
        plt.grid()
        plt.legend(title="Leyenda", shadow=True, fancybox=True)
        plt.title("Polinomio de Lagrange")
        plt.savefig(f"p12_lagrange{number}.pdf",
                    transparent=True, bbox_inches="tight")
        plt.cla()


def plot():
    delta = 0.5
    t = np.linspace(start=-5 - delta, stop=5 + delta, num=300)
    y = 1 / (1 + t**2)
    plt.plot(t, y, lw=0.45, label=r"$f(t)=\frac{1}{1+t^2}$")
    plt.grid()
    plt.legend(title="Leyenda", shadow=True, fancybox=True)
    plt.title("Función de Carl Runge")
    plt.savefig("p12.pdf", transparent=True, bbox_inches="tight")


if __name__ == "__main__":
    plot_lagrange(numbers=numbers)
    plot()
