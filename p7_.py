#!/usr/bin/env python

# Interpolacion de Lagrange
# Polinomio en forma simbólica
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

plt.rcParams["text.usetex"] = True
plt.rcParams["font.serif"] = ["Computer Modern"]

print("INTERPOLACIÓN POLINÓMICA DE LAGRANGE", end="\n\n")
print(
    "Es una forma de presentar el polinomio que interpola un conjunto de puntos dado. ",
    end="\n\n",
)

# INGRESO , Datos de prueba

# Datos de X
xi = np.array([0, 1/2, 1, 2])

# Datos de F(X)
fi = np.array([1, 2, 3/2, -1])

# PROCEDIMIENTO
n = len(xi)
x = sym.Symbol("x")
# Polinomio
polinomio = 0
for i in range(0, n, 1):
    # Termino de Lagrange
    termino = 1
    for j in range(0, n, 1):
        if j != i:
            termino = termino * (x - xi[j]) / (xi[i] - xi[j])
    print("El L(", i, ") es :", termino)
    polinomio = polinomio + termino * fi[i]
# Expande el polinomio
px = polinomio.expand()
# para evaluacion numérica
pxn = sym.lambdify(x, polinomio)

# Puntos para la gráfica
a = np.min(xi)
b = np.max(xi)
muestras = 101
xi_p = np.linspace(a, b, muestras)
fi_p = pxn(xi_p)

# Salida
print("\nPolinomio de Lagrange, expresiones:")
print(polinomio)
print()
print("Polinomio de Lagrange: ")
print(px)

# Gráfica
plt.title("Interpolación de Lagrange")
plt.scatter(xi, fi, s=10, label="Puntos de control")
plt.plot(xi_p, fi_p, 'orange', lw=0.45, label="Polinomio")
plt.legend()
plt.savefig("p7.pdf", transparent=True, bbox_inches="tight")
