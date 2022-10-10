"""
For creating the pseudo measurement data
"""
# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %%
t = np.arange(10, step=0.1)
A = t ** 2 + np.random.random(size=t.shape) * 5 - 2.5
B = np.sin(t) * 10 + 5 + np.random.random(size=t.shape) * 2 - 1

# %%
df = pd.DataFrame(
    data={
        "t": t,
        "A": A,
        "B": B}
)
# %%
df.to_csv("data.csv")
# %%
t = np.arange(10, step=0.1)
R = t ** 2 + np.random.random(size=t.shape) * 5 - 2.5
S = t ** 3 + np.random.random(size=t.shape) * 30 - 15
T = t ** 4 + np.random.random(size=t.shape) * 500 - 250
# %%
df = pd.DataFrame(
    data={
        "t": t,
        "R": R,
        "S": S,
        "T": T}
)
# %%
df.to_csv("data2.csv")
# %%
