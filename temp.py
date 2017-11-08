# -*- coding: utf-8 -*-

import pandas as pd

df = pd.read_csv("0021600001.csv")
for row in df.itertuples():
    if not type(row[6]) is float:
        if row[6].find("Free Throw") != -1:
            print(row[6])
    if not type(row[33]) is float:
        if row[33].find("Free Throw") != -1:
            print(row[33])
