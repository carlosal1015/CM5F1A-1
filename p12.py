#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial

plt.rcParams["text.usetex"] = True
plt.rcParams["font.serif"] = ["Computer Modern"]

numbers = [5, 8, 10]


def plot_lagrange(numbers):
    for number in numbers:
        x = np.linspace(start=-5, stop=5, num=number)
        y = 1 / (1 + x**2)
        poly = lagrange(x, y)
        p = Polynomial(poly.coef[::-1]).coef
        delta = 0.1
        x_new = np.arange(start=-5 - delta, stop=5 + delta, step=0.01)
        plt.plot(x_new, Polynomial(poly.coef[::-1])(x_new), 'orange',
                 lw=0.75, label=f"$0$")
        plt.scatter(x, y, label='data')
        plt.plot(x, y)
        plt.grid()
        plt.legend()
        plt.savefig(f"p12_lagrange{number}.pdf")
        plt.cla()


def plot():
    delta = 0.5
    t = np.linspace(start=-5 - delta, stop=5 + delta, num=300)
    y = 1 / (1 + t**2)
    plt.plot(t, y, lw=0.7, label=r"$f(t)=\frac{1}{1+t^2}$")
    plt.grid()
    plt.legend()
    plt.title("Función de Carl Runge")
    plt.savefig("p12.pdf")


plot_lagrange(numbers=numbers)
plot()
