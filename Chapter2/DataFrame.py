# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
df = pd.DataFrame([
        ['1', 'Fares', 32, True],
        ['2', 'Elena', 23, False],
        ['3', 'Steven', 40, True]])

df.columns = ['id', 'name', 'age', 'decision']

df