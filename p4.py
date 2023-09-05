#!/usr/bin/env python

import sympy as sp

a = sp.Symbol("a", real=True)
b = sp.Symbol("b", real=True)
n = sp.Symbol("n", integer=True, positive=True)
j = sp.Symbol("j", integer=True)
x = sp.Symbol("x", real=True)

lfs = (a+b)**n
rhs = sp.Sum(a, (a, 1, n)).doit()  # sp.Sum(sp.binomial(n, j), ())

lfs_partial_a = sp.diff(lfs, a)
lfs_partial_a_2 = sp.diff(lfs, a, 2)

# print(lfs_partial_a)
# print(lfs_partial_a_2)
print(rhs)
