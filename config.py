"""
Config file for the data files.
Contains all the information neccessary to process the data files.
"""

from dfmeta import DFMeta, Column
import fitfuns

############
# first file
############

datafile = "data.csv"

dfmeta = DFMeta(x_name="t")
dfmeta.add_column(
    Column(
        "A",
        fitfuns.exp_fit
    )
)
dfmeta.add_column(
    Column(
        "B",
        fitfuns.sin_fit
    )
)

#############
# second file
#############

datafile2 = "data2.csv"

dfmeta2 = DFMeta(x_name="t")
dfmeta2.add_column(
    Column(
        "R",
        fitfuns.exp_fit
    )
)
dfmeta2.add_column(
    Column(
        "S",
        fitfuns.exp_fit
    )
)
dfmeta2.add_column(
    Column(
        "T",
        fitfuns.exp_fit
    )
)