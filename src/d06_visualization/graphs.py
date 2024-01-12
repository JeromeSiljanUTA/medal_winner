import itertools

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import rcParams


def draw_MLE(df: pd.DataFrame):
    df = df.sort_values(by=["MLE"])

    plt.bar(df.index, df["MLE"])
    plt.title("MLE of medal round win")
    plt.xticks(rotation=45, ha="right")
    plt.ylabel("Percentage")
    plt.subplots_adjust(bottom=0.2)
    plt.savefig("new.png")
    plt.show()


def draw_dists(df: pd.DataFrame):
    df = df.sort_values(by=["MLE"])
    probabilities = np.linspace(0, 1, 101)

    for idx, row in enumerate(df.iterrows()):
        competitor = row[0]
        dist = row[1].iloc[2]
        plt.plot(probabilities, dist)
        plt.title(competitor)
        plt.xlabel("Percentage of medal round wins")
        plt.ylabel("Likelihood")
        plt.savefig(f"binom_{idx}.png")
        plt.show()
