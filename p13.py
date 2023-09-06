#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["text.usetex"] = True
plt.rcParams["font.serif"] = ["Computer Modern"]

x = np.array([0, 1, 3])
y = np.sqrt(x)

plt.scatter(x, y, label='data')
plt.legend()
plt.savefig("p13.pdf")
