import pandas as pd

from d02_intermediate.transform_int_data import clean_csv
from d04_modelling.binomial import attach_binomial_dists
from d04_modelling.mle import calc_MLE
from d06_visualization.graphs import draw_MLE

df = clean_csv()
df = attach_binomial_dists(df)
df = calc_MLE(df)
draw_MLE(df)
