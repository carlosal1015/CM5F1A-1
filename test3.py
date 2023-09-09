#!/usr/bin/env python

import sympy as sp

_t = [0, 1/2, 1, 2]
_x = [1, 2, 3/2, -1]

t = sp.Symbol("t", nonnegative=True)

l0 = (((t - _t[1]) * (t - _t[2]) * (t - _t[3])) /
      ((_t[0] - _t[1]) * (_t[0] - _t[2]) * (_t[0] - _t[3]))).expand()

l1 = (((t - _t[0]) * (t - _t[2]) * (t - _t[3])) /
      ((_t[1] - _t[0]) * (_t[1] - _t[2]) * (_t[1] - _t[3]))).expand()

l2 = (((t - _t[0]) * (t - _t[1]) * (t - _t[3])) /
      ((_t[2] - _t[0]) * (_t[2] - _t[1]) * (_t[2] - _t[3]))).expand()

l3 = (((t - _t[0]) * (t - _t[1]) * (t - _t[2])) /
      ((_t[3] - _t[0]) * (_t[3] - _t[1]) * (_t[3] - _t[2]))).expand()

p = _x[0] * l0 + _x[1] * l1 + _x[2] * l2 + _x[3] * l3

print(f"l0 = {l0}")
print(f"l1 = {l1}")
print(f"l2 = {l2}")
print(f"l3 = {l3}")
print(f"p = {p}")
