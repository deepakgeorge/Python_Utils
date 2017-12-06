# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 09:03:20 2017

@author: deepa
"""
import pandas as pd
df = pd.DataFrame({'A': [1, 1, 1, 2, 2],
                    'B': range(5),
                    'C': range(5)})
df1 = df.groupby('A').B.agg({'B': ['count','nunique'],'C': ['sum','median']})
df1.columns = ["_".join(x) for x in df1.columns.ravel()]

