import numpy as np
import pandas as pd

#read csv file
d = pd.read_csv('C:/Users/vixky/Desktop/Python Προαιρετική/effects-of-covid-19-on-trade-at-15-december-2021-provisional.csv',sep=',')

#print (for testing)
#print(d.columns)

#find if any null values
print(d.isnull().sum())  
