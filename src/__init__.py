import pandas as pd
from d02_intermediate.transform_int_data import (
    clean_csv,
    get_total_rounds,
    get_total_wins,
)

df = clean_csv()
print(df)
