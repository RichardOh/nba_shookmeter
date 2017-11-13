# -*- coding: utf-8 -*-

import pandas as pd
player = 'Kyrie Irving'
df = pd.read_csv("0021600001.csv")
df = df[ df['PLAYER1_NAME'].str.contains(player) == True]
df = df[ df['EVENTMSGTYPE'].between(1,3) ]