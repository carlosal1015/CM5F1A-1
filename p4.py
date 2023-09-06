#!/usr/bin/env python

import sympy as sp

a = sp.Symbol("a", nonnegative=True)
b = sp.Symbol("b", nonnegative=True)
n = sp.Symbol("n", integer=True, positive=True)
j = sp.Symbol("j", integer=True)
x = sp.Symbol("x", real=True)

lfs = (a+b)**n
rhs = sp.Sum(sp.binomial(n, j) * a ** j * b **(n -j), (j, 1, n)).doit().simplify()

lfs_partial_a = sp.diff(lfs, a).simplify()
lfs_partial_a_2 = sp.diff(lfs, a, 2).simplify()

if __name__ == "__main__":
    print(f"{lfs_partial_a}")
    print(f"{lfs_partial_a_2}")
    print(f"{rhs}")
