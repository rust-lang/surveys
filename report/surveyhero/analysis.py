import pandas as pd


def at_least_one_col(df: pd.DataFrame, yes="Yes", no="No") -> pd.Series:
    """
    Return a series that will contain `yes` for each row in `df` that had at least
    one column not equal to NaN and `no` for the rest.
    """
    return df.notna().any(axis=1).map({True: yes, False: no})
