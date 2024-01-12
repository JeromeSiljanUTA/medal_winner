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
    for mle in df["MLE"]:
        plt.axvline(mle, color=next(color_gen)["color"], linewidth=4.0)

    plt.legend(df.index)
    plt.savefig("new.png")
    plt.show()
