#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

a = sp.Symbol("a", nonnegative=True)
b = sp.Symbol("b", nonnegative=True)
n = sp.Symbol("n", integer=True, positive=True)
j = sp.Symbol("j", integer=True)
x = sp.Symbol("x", real=True)

lfs = (a + b) ** n
rhs = sp.Sum(sp.binomial(n, j) * a**j * b **
             (n - j), (j, 1, n)).doit().simplify()

lfs_partial_a = sp.diff(lfs, a).simplify()
lfs_partial_a_2 = sp.diff(lfs, a, 2).simplify()


plt.rcParams["text.usetex"] = True
plt.rcParams["font.serif"] = ["Computer Modern"]


def b_n(x: np.array, n: int):
    """Retorna la evaluación de B_{n}(x)."""
    from math import comb

    assert np.all(x >= 0) and np.all(
        x <= 1
    ), "t debe estar en el intervalo \left[0, 1\right]."

    return (1 - 1 / n) * x**2 + (1 / n) * x


def plot_b_n(numbers: list):
    """Grafica los polinomios desde k=0,\dotsc,n."""
    x = np.linspace(start=0, stop=1)

    for number in numbers:
        plt.plot(x, b_n(x=x, n=number), lw=0.45,
                 label=f"$B_{{{number}}}(x)$")

    plt.grid()
    plt.legend()
    plt.title(r"Polinomios $B_{n}\left(x\right)$")
    plt.savefig("p4.pdf", transparent=True, bbox_inches="tight")


def check_n0(n0: int, TOLERANCE: float = 1e-6, SAMPLE_SIZE: int = 5000):
    x = np.linspace(start=0, stop=1, num=SAMPLE_SIZE)
    y = np.abs(b_n(x=x, n=n0) - x**2)

    return np.all(y <= TOLERANCE)


if __name__ == "__main__":
    # print(f"{lfs_partial_a}")
    # print(f"{lfs_partial_a_2}")
    # print(f"{rhs}")
    plot_b_n(numbers=[1, 2, 10, 50, 250000])
    valor = check_n0(n0=250000 + 1)
    print(valor)
