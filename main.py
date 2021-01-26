import numpy as np
import pandas as pd

df_dev = pd.read_csv('dev.tsv',sep='\t')
df_eval = pd.read_csv('eval.tsv',sep='\t')

print(df_dev)
print(df_eval)