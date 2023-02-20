# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
x = pd.read_csv('C:\Docs\countries_top10.csv')
data = pd.DataFrame(x)
print(data)

data['Population kmsq'] = data['Population']/data['Area']
print(data)
data['GDP per head'] = data['GDP']/data['Population']
print(data)