import itertools

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import rcParams


def draw_MLE(df: pd.DataFrame):
    color_list = rcParams["axes.prop_cycle"]
    color_gen = itertools.cycle(color_list)

    x = np.linspace(0, 1, 101)
    df = df.sort_values(by=["MLE"])

    plt.bar(df.index, df["MLE"])
    plt.title("MLE of medal round win")
    plt.xticks(rotation=45, ha="right")
    plt.ylabel("Percentage")
    plt.subplots_adjust(bottom=0.2)
    plt.savefig("new.png")
    plt.show()
