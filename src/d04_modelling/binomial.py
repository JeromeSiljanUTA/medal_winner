import numpy as np
import pandas as pd
from scipy.stats import binom


def generate_binomial_dist(win_stats: pd.Series) -> int:
    (
        wins,
        rounds,
    ) = (
        win_stats["Wins"],
        win_stats["Rounds"],
    )

    # Try 21 probabilities
    probability_grid = np.linspace(0, 1, 101)
    dist = binom.pmf(wins, rounds, probability_grid)
    # Normalize
    dist = dist / sum(dist)
    return dist


def attach_binomial_dists(df: pd.DataFrame) -> pd.DataFrame:
    df["Distribution"] = df.apply(generate_binomial_dist, axis=1)
    return df
