# -*- coding: utf-8 -*-

import pandas as pd

df = pd.read_csv("0021600001.csv")

for str in df['HOMEDESCRIPTION'].iteritems():
    if str[1].find("Free Throw") != -1:
        print(str)