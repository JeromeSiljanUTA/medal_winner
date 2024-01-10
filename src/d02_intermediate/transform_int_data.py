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
    round_counts = df.groupby("Competitor")["Competitor"].count()
    names = round_counts[round_counts >= 5].index
    df = df[df["Competitor"].isin(names)].reset_index(drop=True)
    df["Success"] = df["Success"] == "Win"
    return df


def get_total_wins(df: pd.DataFrame) -> pd.Series:
    return df.groupby("Competitor")["Success"].sum()


def get_total_rounds(df: pd.DataFrame) -> pd.Series:
    return df.groupby("Competitor")["Competitor"].count()
