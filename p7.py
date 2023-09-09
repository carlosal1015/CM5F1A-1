#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial
import sympy as sp

t = sp.Symbol('t', real=True)
l_0 = -t**3 + 7 / 2*t**2 - 7/2 * t +1
l_1 = 8 / 3 * t**3 - 8*t**2 +16/3*t
l_2 = -2*t**3 + 5 * t**2 - 2*t
l_3 = 1 /3 *t**3 -1/2 *t**2 + 1/6 *t
p_lagrange = (1*l_0 + 2*l_1 + 3/2 * l_2 - l_3).simplify()
print(p_lagrange)

plt.rcParams["text.usetex"] = True
plt.rcParams["font.serif"] = ["Computer Modern"]

x = np.array([0, 1/2, 1, 2])
y = np.array([1, 2, 3/2, -1])
poly = lagrange(x, y)
# print(poly)
p = Polynomial(poly.coef[::-1]).coef
# print(p)
delta = 0.1
x_new = np.arange(start=-1 - delta, stop=1 + delta, step=0.01)


plt.scatter(x, y, s=10, label='Puntos de control')
plt.plot(x_new, Polynomial(
    poly.coef[::-1])(x_new), 'orange', lw=0.45, label=f"$p_3(t)={{{p[3]}}}t^3{{{p[2]}}}t^2{{{p[1]}}}t+{{{p[0]}}}$")
plt.grid()
plt.legend(title="Leyenda", shadow=True, fancybox=True)
plt.title(f"Polinomio interpolador de Lagrange $p_3(t)$")
plt.savefig("p7.pdf", transparent=True, bbox_inches="tight")

plt.cla()
plt.scatter(x, np.zeros_like(x), s=10)
plt.plot(x_new, 0.5*x_new*(x_new-1), lw=0.45, label=r"$\ell_{0}(t)=-t^3+\frac{7}{2}t^2-\frac{7}{2}t+1$")
plt.plot(x_new, -(x_new+1)*(x_new-1), lw=0.45, label=r"$\ell_{1}(t)=\frac{8}{3}t^3-8t^2+\frac{16}{3}t$")
plt.plot(x_new, 0.5*(x_new+1)*x_new, lw=0.45, label=r"$\ell_{2}(t)=-2t^3+5t^2-2t$")
plt.grid()
plt.legend(title="Leyenda", shadow=True, fancybox=True)
plt.title(f"Funciones base de Lagrange")
plt.savefig("p7_lagrange.pdf", transparent=True, bbox_inches="tight")
