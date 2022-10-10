import pandas as pd

def get_data(data_path) -> pd.DataFrame:
    """
    Load a data file and return dataframe. Uses the first column as index.
    """
    return pd.read_csv(data_path, index_col=0)
