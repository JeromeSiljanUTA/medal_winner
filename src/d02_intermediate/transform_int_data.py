"""
Load data to DataFrame.
"""

import pandas as pd
import numpy as np
from scipy.stats import binom
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

    wins = get_total_wins(df)
    rounds = get_total_rounds(df)
    return pd.DataFrame([wins, rounds]).T


def get_total_wins(df: pd.DataFrame) -> pd.Series:
    return df.groupby("Competitor")["Success"].sum().rename("Wins")


def get_total_rounds(df: pd.DataFrame) -> pd.Series:
    return df.groupby("Competitor")["Competitor"].count().rename("Rounds")


def generate_binomial_dist(win_stats: pd.Series) -> int:
    (
        wins,
        rounds,
    ) = (
        win_stats["Wins"],
        win_stats["Rounds"],
    )

    # Try 21 probabilities
    probability_grid = np.linspace(0, 1, 21)
    dist = binom.pmf(wins, rounds, probability_grid)
    return dist


def attach_binomial_dists(df: pd.DataFrame) -> pd.DataFrame:
    df["Distribution"] = df.apply(generate_binomial_dist, axis=1)
    return df
