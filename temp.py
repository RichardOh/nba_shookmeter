# -*- coding: utf-8 -*-

import pandas as pd

df = pd.read_csv("0021600001.csv")
df_home = df[df["HOMEDESCRIPTION"].str.contains("Free Throw") == True]["HOMEDESCRIPTION"]
df_away = df[df["VISITORDESCRIPTION"].str.contains("Free Throw") == True]["VISITORDESCRIPTION"]