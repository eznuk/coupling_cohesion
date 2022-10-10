from dataclasses import dataclass
from typing import Callable

@dataclass
class Column:
    """
    Class representing a column of a data file.
    Contains the name and the corresponding fit function.
    """
    name: str
    fitfun: Callable

class DFMeta:
    """
    Class containing the metadata of a data file.
    Contains the name of the x vector (x_name) and a list of columns
    which are added by add_column(column).
    """
    def __init__(self, x_name):
        self.columns = []
        self.x_name = x_name

    def add_column(self, column):
        self.columns.append(column)