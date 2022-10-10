from scipy.optimize import curve_fit
from typing import Callable, List
import numpy as np
import pandas as pd

from dfmeta import DFMeta

def fit(fun: Callable, x: np.array, y: np.array) -> np.array:
    """
    Fits y over x using fun.
    Returns a list of the optimal parameters of fun.
    """
    popt, _ = curve_fit(fun, x, y)
    return popt

def get_fitted_y(fun: Callable, x: np.array, popt: np.array) -> np.array:
    """
    Returns the y values of a function corresponding to a fit 
    using the parameters popt.
    """
    return fun(x, *popt)

def fit_df(df: pd.DataFrame, dfmeta: DFMeta):
    """
    Fill all columns in df using dfmeta as meta data.
    Results are saved in the column entries of dfmeta as
    column.popt and column.fitted_y
    """
    for column in dfmeta.columns:
        popt = fit(column.fitfun, df[dfmeta.x_name], df[column.name])
        fitted_y = get_fitted_y(column.fitfun, df[dfmeta.x_name], popt)
        column.popt = popt
        column.fitted_y = fitted_y