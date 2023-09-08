#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial
import sympy as sp

t = sp.Symbol('t', real=True)
l_0 = 0.5*t*(t-1)
l_1 = -(t+1)*(t-1)
l_2 = 0.5*(t+1)*t
p_lagrange = (0.5*l_0 + l_1 -l_2).simplify()
print(p_lagrange)

plt.rcParams["text.usetex"] = True
plt.rcParams["font.serif"] = ["Computer Modern"]

x = np.array([-1, 0, 1])
y = np.array([1/2, 1, -1])
poly = lagrange(x, y)
# print(poly)
p = Polynomial(poly.coef[::-1]).coef
# print(p)
delta = 0.1
x_new = np.arange(start=-1 - delta, stop=1 + delta, step=0.01)


plt.scatter(x, y, s=10, label='Puntos de control')
plt.plot(x_new, Polynomial(
    poly.coef[::-1])(x_new), 'orange', lw=0.75, label=f"${{{p[2]}}}x^2{{{p[1]}}}x+{{{p[0]}}}$")
plt.grid()
plt.legend()
plt.title(f"Polinomio de interpolación de Lagrange")
plt.savefig("p6.pdf")

plt.cla()
plt.plot(x_new, 0.5*x_new*(x_new-1), lw=0.75, label=f"$\ell_{0}(t)$")
plt.plot(x_new, -(x_new+1)*(x_new-1), lw=0.75, label=f"$\ell_{1}(t)$")
plt.plot(x_new, 0.5*(x_new+1)*x_new, lw=0.75, label=f"$\ell_{2}(t)$")
plt.grid()
plt.legend()
plt.title(f"Polinomios de Lagrange")
plt.savefig("p6_lagrange.pdf")
