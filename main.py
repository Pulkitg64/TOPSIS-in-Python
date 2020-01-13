# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 17:32:43 2020

@author: pulki
"""
import pandas as pd
import TOPSIS.py
    
dataset = pd.read_csv('data.csv')
dt = pd.read_csv('data.csv')
dataset = dataset.iloc[:,1:].values
c = [1,1,1,1]
impact = ["+", "+", "-", "+"]

p = TOPSIS.topsis(dataset,impact,c)

print(p)

