#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["text.usetex"] = True
plt.rcParams["font.serif"] = ["Computer Modern"]

n = 10
x = np.arange(start=-5, stop=5, step=n)
y = 1 / (1 + x**2)

plt.scatter(x, y, label='data')
plt.plot(x, y)
plt.legend()
plt.savefig("p12.pdf")
