"""
Load data to DataFrame.
"""

import pandas as pd
import sys
import os


def clean_csv() -> pd.DataFrame:
    medal_data_path = os.path.join("data", "01_raw", "medal_data.csv")
    # Fix path if called from ntoebook
    if not os.path.exists(medal_data_path):
        medal_data_path = os.path.join("../", "data", "01_raw", "medal_data.csv")

    df = pd.read_csv(medal_data_path)
    return df


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    return df
