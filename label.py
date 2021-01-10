# -*- coding: utf-8 -*-
"""
@author: hrithikv
"""

import pandas as pd
data = pd.read_csv('final.csv',index_col=0)
data.head()
data['comment'].str.contains(lexicon).astype(int).sum()
lexicon = ''
data['rating'] = data['comment'].str.contains(lexicon)
data.to_csv('labeled.csv')
data.head()
abuse = data[data.rating == True]
