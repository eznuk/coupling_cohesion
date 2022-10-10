import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from dfmeta import DFMeta

def plot_data(df: pd.DataFrame):
    """
    Plots the data of a specific dataframe.
    """
    df.plot(x="t", y=["A", "B"])

def plot_fit(x: np.array, y_data: np.array, y_fit: np.array):
    """
    Fits the x and y data and the corresponding fit.
    """
    fig, ax = plt.subplots()
    ax.scatter(x, y_data, label="data")

    ax.plot(
        x,
        y_fit,
        linewidth=3,
        color="k",
        label="fit")

def plot_data2(df: pd.DataFrame, dfmeta: DFMeta):
    """
    Plots the data of a general dataframe df using the metadata
    provided by dfmeta.
    """
    # collect all column names
    cols = [column.name for column in dfmeta.columns]
    df.plot(x=dfmeta.x_name, y=cols)

def plot_df_fits(df: pd.DataFrame, dfmeta: DFMeta):
    """
    Plots all fits of a dataframe df using the metadata provided by dfmeta.
    """
    for column in dfmeta.columns:
        plot_fit(df[dfmeta.x_name], df[column.name], column.fitted_y)
