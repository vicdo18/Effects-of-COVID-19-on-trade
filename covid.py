import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import plotly.graph_objects as go 

#read csv file
df = pd.read_csv('effects-of-covid-19-on-trade-at-15-december-2021-provisional.csv',sep=',')

#print (for testing)
# print(df.columns)

#find if any null values
#print(df.isnull().sum())             #no null values

#------------------------------------- ER1 ------------------------------------------------------------#
#Συνολική παρουσίαση του τζίρου (στήλη value) ανά μήνα (στις αντίστοιχες μονάδες μέτρησης)

# Convert the Date column to a datetime type and set it as the index   - for better parsing 
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
# print(df)

# Extract the month and year from the 'Date' column
df['Month'] = df.index.month   
df['Year'] = df.index.year

grouped_df = df.groupby(['Year', 'Month', 'Measure'])['Value'].sum().reset_index()
print(grouped_df)                                     # why 167 - (7years*12months*2measures) = 168 - 1  because of the header

#--------------------------------------------------#

# Separate the data for the two units of measurement ('Tonnes' and '$')
tonnes_df = grouped_df[grouped_df['Measure'] == 'Tonnes']
# print(tonnes_df) 
dollars_df = grouped_df[grouped_df['Measure'] == '$']
# print(dollars_df)

#--------------------------------------------------#

# for i in df['Month'] :
#     sum=0
#     for j in df['Year'] :
#         for k in tonnes_df :
#             sum = sum + df['Value']
#         print(sum)

#Get sum of Tonnes for each month of each year
tonnes_df = tonnes_df.groupby(['Year', 'Month'])['Value'].sum().reset_index()


#Get sum of Dollars for each month of each year
dollars_df = dollars_df.groupby(['Year', 'Month'])['Value'].sum().reset_index()

#--------------------------------------------------#


#measure in millions
# tonnes_df['Value'] = tonnes_df['Value'] / 1000000                                     #aplopoihsh 
# dollars_df['Value'] = dollars_df['Value'] / 1000000

#show only measure for $
#dollars_df = dollars_df.drop(columns=['Year', 'Month'])
# print(dollars_df)           #toulaxiston o arithmos sthlwn einai swstos


# print(tonnes_df)
# print(dollars_df)



# Plot the turnover by month for Tonnes using a pie chart
# plt.figure(figsize=(6, 6))
# plt.pie(tonnes_df['Value'], labels=tonnes_df['Month'], autopct='%1.1f%%')
# plt.title('Turnover by Month (Tonnes)')
# plt.show()

# # Plot the turnover by month for Tonnes using a bar chart
# plt.figure(figsize=(10, 6))
# plt.bar(tonnes_df['Month'], tonnes_df['Value'])
# plt.xlabel('Month')
# plt.ylabel('Turnover')
# plt.title('Turnover by Month (Tonnes)')
# plt.show()


#------------------------------------- ER2 ------------------------------------------------------------#
