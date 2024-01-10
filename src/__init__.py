import pandas as pd
from d02_intermediate.transform_int_data import (
    clean_csv,
    attach_binomial_dists,
)

df = clean_csv()
df = attach_binomial_dists(df)
df
