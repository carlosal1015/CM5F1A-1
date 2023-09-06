#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np


plt.rcParams["text.usetex"] = True
plt.rcParams["font.serif"] = ["Computer Modern"]


def b_n(t: np.array, n: int):
    """Retorna la evaluación de B_{n}(t)."""
    from math import comb

    assert np.all(t >= 0) and np.all(
        t <= 1
    ), "t debe estar en el intervalo \left[0, 1\right]."

    return (1 - 1 / n) * t**2 + (1 / n) * t


def plot_b_n(numbers: list):
    """Grafica los polinomios de Bernstein desde k=0,\dotsc,n."""
    t = np.linspace(start=0, stop=1)

    for number in numbers:
        plt.plot(t, b_n(t=t, n=number), lw=0.75, label=f"$B_{number}$")

    plt.grid()
    plt.legend()
    plt.title(r"Polinomios $B_{n}\left(t\right)$")


plot_b_n(numbers=[1, 2, 3, 4, 5, 6, 7, 8])
plt.savefig("b_n.pdf")

TOLERANCE = 1e-6
t = np.linspace(start=0, stop=1, num=10)
y = b_n(t=t, n=1)
print(y)
print(np.all(np.abs(y) <= TOLERANCE))
