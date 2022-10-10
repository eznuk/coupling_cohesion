# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
# %%
# load data
df = pd.read_csv("data.csv", index_col=0)
# plot data
df.plot(x="t", y=["A", "B"])
# %%
# fit data
def fitfun(t, a):
    return t ** a

popt1, _ = curve_fit(fitfun, df["t"], df["A"])

# %%
# plot result
fig, ax = plt.subplots()
ax.scatter(df["t"], df["A"], label="data")
ax.plot(
    df["t"],
    fitfun(df["t"], popt1[0]),
    linewidth=3,
    color="k",
    label="fit")
ax.legend()
# %%
# now the second column
# fit data
def fitfun2(t, a, b):
    return np.sin(t) * a + b

popt2, _ = curve_fit(fitfun2, df["t"], df["B"])

fig, ax = plt.subplots()
ax.scatter(df["t"], df["B"], label="data")
ax.plot(
    df["t"],
    fitfun2(df["t"], popt2[0], popt2[1]),
    linewidth=3,
    color="k",
    label="fit")
ax.legend()
# %%
