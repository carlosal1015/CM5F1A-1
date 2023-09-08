#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["text.usetex"] = True
plt.rcParams["font.serif"] = ["Computer Modern"]


def bernstein(t: np.array, k: int, n: int):
    """Retorna la evaluación de B_{k,n}(t)."""
    from math import comb

    assert k in range(
        n + 1), "k debe pertenecer a \left[0, n\right] \cap \mathbb{Z}."
    assert np.all(t >= 0) and np.all(
        t <= 1
    ), "t debe estar en el intervalo \left[0, 1\right]."

    return comb(n, k) * t**k * (1 - t) ** (n - k)


k = 3
n = 5
t = np.linspace(start=0, stop=1, num=100)
kappa = (40 * t**3 - 120 * t**2 + 60 * t) / (
    1 + (50 * t**4 - 80 * t**3 + 30 * t**2) ** 2
) ** (3 / 2)

plt.plot(t, bernstein(t=t, k=k, n=n), lw=0.75, label=f"$B_{{{k},{n}}}(t)$")
plt.grid()
plt.legend()
plt.title(f"Polinomio de Bernstein $B_{{{k},{n}}}(t)$")
plt.savefig("p1.pdf", transparent=True, bbox_inches="tight")
plt.cla()

plt.plot(t, kappa, lw=0.75, label=f"${{\kappa}}(t)$")
plt.grid()
plt.legend()
plt.title(f"Función curvatura ${{\kappa}}(t)$")
plt.savefig("p1_curvature.pdf", transparent=True, bbox_inches="tight")
