#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial

plt.rcParams["text.usetex"] = True
plt.rcParams["font.serif"] = ["Computer Modern"]

x = np.array([-1, 0, 1])
y = np.array([1/2, 1, -1])
poly = lagrange(x, y)
print(poly)

p = Polynomial(poly.coef[::-1]).coef
print(p)
delta = 0.1
x_new = np.arange(start=-1 - delta, stop=1 + delta, step=0.1)

plt.scatter(x, y, label='data')
plt.plot(x_new, Polynomial(poly.coef[::-1])(x_new), label='Polynomial')
plt.legend()
plt.savefig("p6.pdf")
