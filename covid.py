import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#read csv file
df = pd.read_csv('effects-of-covid-19-on-trade-at-15-december-2021-provisional.csv',sep=',')

#print (for testing)
#print(df.columns)

#find if any null values
print(df.isnull().sum())             #no null values

#------------------------------------- ER1 ------------------------------------------------------------#
#Συνολική παρουσίαση του τζίρου (στήλη value) ανά μήνα (στις αντίστοιχες μονάδες μέτρησης)

# Set the 'Date' column as the index
# Convert the Date column to a datetime type and set it as the index
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Resample the data by month and sum the 'Value' column in USD and the 'Netweight (kg)' column in tonnes
monthly_turnover = df['Value'].resample('M').sum()
# different for tonnes and $