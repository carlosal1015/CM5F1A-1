#!/usr/bin/env python

import sympy as sp

t = sp.Symbol("t", nonnegative=True)
B_13 = (3 * t * (1 - t) ** 2).expand()
B_23 = (3 * t**2 * (1 - t)).expand()
B_24 = (6 * t**2 * (1 - t) ** 2).expand()
B_33 = (t**3).expand()
B_34 = (4 * t**3 * (1 - t)).expand()
B_35 = (10 * t**3 * (1 - t) ** 2).expand()

B_prime_35 = 5 * (B_24 - B_34)
B_prime_prime_35 = 5 * 4 * (B_13 - 2 * B_23 + B_33)

kappa = (B_prime_prime_35 / (1 + B_prime_35**2) ** (3 / 2))#.simplify()

print(f"B_13 = {B_13}")
print(f"B_23 = {B_23}")
print(f"B_24 = {B_24}")
print(f"B_33 = {B_33}")
print(f"B_34 = {B_34}")
print(f"B_35 = {B_35}")
print(f"B_prime_35 = {B_prime_35}")
print(f"B_prime_prime_35 = {B_prime_prime_35}")
print(f"kappa = {kappa}")
