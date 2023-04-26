import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#read csv file
df = pd.read_csv('effects-of-covid-19-on-trade-at-15-december-2021-provisional.csv',sep=',')

#print (for testing)
#print(df.columns)

#find if any null values
#print(df.isnull().sum())             #no null values

#------------------------------------- ER1 ------------------------------------------------------------#
#Συνολική παρουσίαση του τζίρου (στήλη value) ανά μήνα (στις αντίστοιχες μονάδες μέτρησης)

# Set the 'Date' column as the index
# Convert the Date column to a datetime type and set it as the index
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Resample the data by month and sum the 'Value' column in USD and the 'Netweight (kg)' column in tonnes
monthly_turnover = df['Value'].resample('M').sum()
monthly_weight = df['Tonnes'].resample('M').sum() / 1000  # Convert from kg to tonnes

# Create a line chart with monthly turnover and weight
fig, ax1 = plt.subplots()
ax1.set_xlabel('Month')
ax1.set_ylabel('Turnover (USD)')
ax1.plot(monthly_turnover.index, monthly_turnover.values, color='blue')
ax2 = ax1.twinx()
ax2.set_ylabel('Weight (tonnes)')
ax2.plot(monthly_weight.index, monthly_weight.values, color='green')
fig.tight_layout()
plt.show()