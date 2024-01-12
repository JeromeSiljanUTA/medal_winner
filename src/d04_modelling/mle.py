import numpy as np
import pandas as pd


def calc_MLE(df: pd.DataFrame) -> pd.DataFrame:
    df["MLE"] = df["Wins"] / df["Rounds"]
    return df
