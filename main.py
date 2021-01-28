import numpy as np
import pandas as pd
from category_encoders import *
import category_encoders as ce
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import category_encoders as ce
from sklearn.preprocessing import LabelEncoder
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import GridSearchCV











df_dev = pd.read_csv('dev.tsv', sep='\t', index_col=0)
df_eval = pd.read_csv('eval.tsv', sep='\t', index_col=0)
df = pd.concat([df_dev, df_eval], sort=False)
# print(df.isna().any())
# print(df_dev.isna().any())
# print(df.columns)
df_1h = pd.get_dummies(df,columns=['designation', 'province', 'region_1', 'region_2','variety', 'winery'])





