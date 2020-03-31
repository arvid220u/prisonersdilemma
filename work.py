#%%
# imports
import numpy as np
import sympy as sym

# %%
# constants
p = sym.Symbol('p')

# %%
# pavlov vs allC
M = sym.Matrix([[(1-p)**2,    (1-p)*p,    p*(1-p),    p**2],
              [p**2,        p*(1-p),    (1-p)*p,    (1-p)**2],
              [p**2,        p*(1-p),    (1-p)*p,    (1-p)**2],
              [(1-p)**2,    p*(1-p),    (1-p)*p,    p**2]])

# %%
sym.simplify(M**10)

# %%
M_pavlovVSallc = sym.Matrix([[1-p, p],[p,1-p]])

sym.simplify(M_pavlovVSallc**10)

# %%
