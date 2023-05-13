import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import mysql 
import mysql.connector

#read csv file
df = pd.read_csv('effects-of-covid-19-on-trade-at-15-december-2021-provisional.csv',sep=',')

#print (for testing)
# print(df.columns)

#find if any null values
#print(df.isnull().sum())             #no null values

#------------------------------------- ER1 ------------------------------------------------------------#
#Συνολική παρουσίαση του τζίρου (στήλη value) ανά μήνα (στις αντίστοιχες μονάδες μέτρησης).

# Convert the Date column to a datetime type and set it as the index   - for better parsing 
df['Date'] = pd.to_datetime(df['Date'],dayfirst=True)
df.set_index('Date', inplace=True)
#print(df)                                        # 2015-01-01 - 2021-12-15

# Extract the month and year from the 'Date' column - nomizw den xreiazetai
df['Month'] = df.index.month   
df['Year'] = df.index.year

grouped_first_df=df.groupby(['Year','Month','Measure'])[["Value"]].sum().reset_index()
# print(grouped_first_df)      #TELEIA OLA OK                            

tonnes_df = grouped_first_df[grouped_first_df['Measure'] == 'Tonnes']
dollar_df = grouped_first_df[grouped_first_df['Measure'] == '$']

# print(tonnes_df)
# print(dollar_df)

#parse dataframes to lists
tonnes_df_list = tonnes_df['Value'].tolist()
dollar_df_list = dollar_df['Value'].tolist()

# print (tonnes_df_list)
# print (dollar_df_list)

###################plot $ and Tonnes value per month per year ###########################################

# months = tonnes_df['Month']   #???
# fig, ax = plt.subplots()

# labels = [f"{m}-{y}" for m, y in zip(months, years)]
# ax.set_xticks(np.arange(len(labels)))
# ax.set_xticklabels(labels)

# ax.bar(np.arange(len(values)), values, color='orange')
# ax.set_xlabel('Month-Year')
# ax.set_ylabel('Tonnes')
# ax.set_title('Tonnes per Month')
# plt.xticks(rotation=90)
# # plt.show()

# values = dollar_df['Value']
# fig, ax = plt.subplots()

# labels = [f"{m}-{y}" for m, y in zip(months, years)]
# ax.set_xticks(np.arange(len(labels)))
# ax.set_xticklabels(labels)

# ax.bar(np.arange(len(values)), values)

# ax.set_xlabel('Month-Year')
# ax.set_ylabel('Dollars')
# ax.set_title('Dollars per Month')
# plt.xticks(rotation=90)
# plt.show()
#######################################################################################

#------------------------------------- ER2 ------------------------------------------------------------#

#Συνολική παρουσίαση του τζίρου (στήλη value) ανά χώρα (στις αντίστοιχες μονάδες μέτρησης).  

grouped_second_df=df.groupby(['Country','Measure'])[["Value"]].sum().reset_index()
# print(grouped_second_df)  

# i need to divide the dataframe into 2 dataframes, one for $ and one for tonnes
tonnes_df = grouped_second_df[grouped_second_df['Measure'] == 'Tonnes']
dollar_df = grouped_second_df[grouped_second_df['Measure'] == '$']

# print(tonnes_df)
# print(dollar_df)

#parse dataframes to lists
country_tonnes_df_list = tonnes_df['Value'].tolist()
country_dollar_df_list = dollar_df['Value'].tolist()

# print (country_tonnes_df_list)
# print (country_dollar_df_list)

#plot $ and Tonnes value per country ###########################################

#dollars
# countries = dollar_df['Country']
# values = dollar_df['Value']

# fig, ax = plt.subplots()

# labels = [f"{c}" for c in countries]
# ax.set_xticks(np.arange(len(labels)))
# ax.set_xticklabels(labels)

# ax.bar(np.arange(len(values)), values)

# ax.set_xlabel('Country')
# ax.set_ylabel('Dollars')
# ax.set_title('Dollars per Country')
# plt.xticks(rotation=90)
# plt.show()

# #tonnes 
# countries = tonnes_df['Country']
# values = tonnes_df['Value']

# fig, ax = plt.subplots()

# labels = [f"{c}" for c in countries]
# ax.set_xticks(np.arange(len(labels)))
# ax.set_xticklabels(labels)

# ax.bar(np.arange(len(values)), values, color='orange')

# ax.set_xlabel('Country')
# ax.set_ylabel('Tonnes')
# ax.set_title('Tonnes per Country')
# plt.xticks(rotation=90)
# plt.show()

#------------------------------------- ER3 ------------------------------------------------------------#
# Συνολική παρουσίαση του τζίρου (στήλη value) για κάθε μέσο μεταφοράς (στις αντίστοιχες μονάδες μέτρησης)

grouped_third_df=df.groupby(['Transport_Mode','Measure'])[["Value"]].sum().reset_index()
# print(grouped_third_df)

# i need to divide the dataframe into 2 dataframes, one for $ and one for tonnes
transport_tonnes_df = grouped_third_df[grouped_third_df['Measure'] == 'Tonnes']
transport_dollar_df = grouped_third_df[grouped_third_df['Measure'] == '$']

# print(transport_tonnes_df)
# print(transport_dollar_df)


#plot $ and Tonnes value per transport ###########################################

# #dollars
# transports = transport_dollar_df['Transport_Mode']
# values = transport_dollar_df['Value']

# fig, ax = plt.subplots()

# labels = [f"{t}" for t in transports]
# ax.set_xticks(np.arange(len(labels)))
# ax.set_xticklabels(labels)

# ax.bar(np.arange(len(values)), values)

# ax.set_xlabel('Transport')
# ax.set_ylabel('Dollars')
# ax.set_title('Dollars per Transport')
# plt.xticks(rotation=90)
# plt.show()

# #tonnes
# transports = transport_tonnes_df['Transport_Mode']
# values = transport_tonnes_df['Value']

# fig, ax = plt.subplots()

# labels = [f"{t}" for t in transports]
# ax.set_xticks(np.arange(len(labels)))
# ax.set_xticklabels(labels)

# ax.bar(np.arange(len(values)), values, color='orange')

# ax.set_xlabel('Transport')
# ax.set_ylabel('Tonnes')
# ax.set_title('Tonnes per Transport')
# plt.xticks(rotation=90)
# plt.show()


##############################################################################

#------------------------------------- ER4 ------------------------------------------------------------#
#Συνολική παρουσίαση του τζίρου (στήλη value) για κάθε μέρα της εβδομάδας (στις αντίστοιχες μονάδες μέτρησης)

grouped_fourth_df=df.groupby(['Weekday','Measure'])[["Value"]].sum().reset_index()
# print(grouped_fourth_df)

weekday_tonnes_df = grouped_fourth_df[grouped_fourth_df['Measure'] == 'Tonnes']
weekday_dollar_df = grouped_fourth_df[grouped_fourth_df['Measure'] == '$']

# print(weekday_tonnes_df)
# print(weekday_dollar_df)

# lists
weekday_tonnes_df_list = weekday_tonnes_df['Value'].tolist()
weekday_dollar_df_list = weekday_dollar_df['Value'].tolist()

#plot $ and Tonnes value per weekday ###########################################

# #dollars
# weekdays = weekday_dollar_df['Weekday']
# values = weekday_dollar_df['Value']

# fig, ax = plt.subplots()

# labels = [f"{w}" for w in weekdays]
# ax.set_xticks(np.arange(len(labels)))
# ax.set_xticklabels(labels)

# ax.bar(np.arange(len(values)), values)

# ax.set_xlabel('Weekday')
# ax.set_ylabel('Dollars')
# ax.set_title('Dollars per Weekday')
# plt.xticks(rotation=90)
# plt.show()

# #tonnes
# weekdays = weekday_tonnes_df['Weekday']
# values = weekday_tonnes_df['Value']

# fig, ax = plt.subplots()

# labels = [f"{w}" for w in weekdays]
# ax.set_xticks(np.arange(len(labels)))
# ax.set_xticklabels(labels)

# ax.bar(np.arange(len(values)), values, color='orange')

# ax.set_xlabel('Weekday')
# ax.set_ylabel('Tonnes')
# ax.set_title('Tonnes per Weekday')
# plt.xticks(rotation=90)
# plt.show()

#------------------------------------- ER5 ------------------------------------------------------------#
#Συνολική παρουσίαση του τζίρου (στήλη value) για κάθε κατηγορία εμπορεύματος (στις αντίστοιχες μονάδες μέτρησης)

grouped_fifth_df=df.groupby(['Commodity','Measure'])[["Value"]].sum().reset_index()
# print(grouped_fifth_df)

commodity_tonnes_df = grouped_fifth_df[grouped_fifth_df['Measure'] == 'Tonnes']
commodity_dollar_df = grouped_fifth_df[grouped_fifth_df['Measure'] == '$']

# lists
commodity_tonnes_df_list = commodity_tonnes_df['Value'].tolist()
commodity_dollar_df_list = commodity_dollar_df['Value'].tolist()

#plot $ and Tonnes value per commodity ###########################################

# #dollars
# commodities = commodity_dollar_df['Commodity']
# values = commodity_dollar_df['Value']

# fig, ax = plt.subplots()

# labels = [f"{c}" for c in commodities]
# ax.set_xticks(np.arange(len(labels)))
# ax.set_xticklabels(labels)

# ax.bar(np.arange(len(values)), values)

# ax.set_xlabel('Commodity')
# ax.set_ylabel('Dollars')
# ax.set_title('Dollars per Commodity')
# plt.xticks(rotation=90)
# plt.show()

# #tonnes
# commodities = commodity_tonnes_df['Commodity']
# values = commodity_tonnes_df['Value']

# fig, ax = plt.subplots()

# labels = [f"{c}" for c in commodities]
# ax.set_xticks(np.arange(len(labels)))
# ax.set_xticklabels(labels)

# ax.bar(np.arange(len(values)), values, color='orange')

# ax.set_xlabel('Commodity')
# ax.set_ylabel('Tonnes')
# ax.set_title('Tonnes per Commodity')
# plt.xticks(rotation=90)
# plt.show()

# #plot pie chart - tonnes
# fig, ax = plt.subplots()
# ax.pie(commodity_tonnes_df_list, labels=commodity_tonnes_df['Commodity'], autopct='%1.1f%%', shadow=True, startangle=90)
# #make text same color as pie pieces
# for text in ax.texts:
#     text.set_size(6)
#     text.set_color(ax.patches[ax.texts.index(text)].get_facecolor())
# ax.axis('equal') 
# ax.set_title('Tonnes per Commodity')
# plt.show()

# #plot pie chart - dollars
# fig, ax = plt.subplots()
# ax.pie(commodity_dollar_df_list, labels=commodity_dollar_df['Commodity'], autopct='%1.1f%%', shadow=True, startangle=90)
# for text in ax.texts:
#     text.set_size(6)
#     text.set_color(ax.patches[ax.texts.index(text)].get_facecolor())
# ax.axis('equal')  
# ax.set_title('Dollars per Commodity')
# plt.show()

#------------------------------------- ER6 ------------------------------------------------------------#
#Παρουσίαση των 5 μηνών με το μεγαλύτερο τζίρο, ανεξαρτήτως μέσου μεταφοράς και είδους ανακυκλώσιμων ειδών

grouped_sixth_df=df.groupby(['Year','Month'])[["Value"]].sum().reset_index().sort_values(by=['Value'], ascending=False).head(5)   #both $ and tonnes
# print(grouped_sixth_df)

# lists
grouped_sixth_df_list = grouped_sixth_df['Value'].tolist()

# #plot values
# months = grouped_sixth_df['Month']
# values = grouped_sixth_df['Value']

# fig, ax = plt.subplots()

# labels = [f"{m}" for m in months]
# ax.set_xticks(np.arange(len(labels)))
# ax.set_xticklabels(labels)

# ax.bar(np.arange(len(values)), values, color='orange')

# ax.set_xlabel('Month')
# ax.set_ylabel('Value($ and Tonnes))')
# ax.set_title('Value per Month')
# plt.xticks(rotation=90)
# plt.show()

#------------------------------------- ER7 ------------------------------------------------------------#
#Παρουσίαση των 5 κατηγοριών εμπορευμάτων με το μεγαλύτερο τζίρο, για κάθε χώρα
#Presentation of the 5 categories of goods with the highest turnover, for each country(sos)

# Sort the data by 'Country' and 'Turnover' in descending order
sorted_data = df.sort_values('Value', ascending=False)

# Group the sorted data by 'Country' and get the top five categories for each group
grouped_data = sorted_data.groupby('Country').head(5)

#commodities for each country must be unique
#grouped_data = grouped_data.drop_duplicates(subset=['Country', 'Commodity'])

# Print the result
# print(grouped_data)

#------------------------------------- ER8 ------------------------------------------------------------#
#- Παρουσίαση της ημέρας με το μεγαλύτερο τζίρο, για κάθε κατηγορία εμπορεύματος
#- Presentation of the day with the highest turnover, for each category of goods

# # Sort the data by 'Commodity' and 'Turnover' in descending order
# sorted_data = df.sort_values('Value', ascending=False)
# # print(sorted_data)

# # Group the sorted data by 'Commodity' and get the top five categories for each group
# grouped_data = sorted_data.groupby('Commodity').head(1)

# # Print the result
# print(grouped_data)

# #make list
# grouped_eight_list = grouped_data['Value'].tolist()

# #plot 
# commodities = grouped_data['Commodity']
# values = grouped_data['Value']

# fig, ax = plt.subplots()

# labels = [f"{c}" for c in commodities]
# ax.set_xticks(np.arange(len(labels)))
# ax.set_xticklabels(labels)

# ax.bar(np.arange(len(values)), values, color='orange')

# ax.set_xlabel('Commodity')
# ax.set_ylabel('Value($ and Tonnes))')
# ax.set_title('Value per Commodity')
# plt.xticks(rotation=90)
# plt.show()

#-------------------------------------------------------------MySQL Connection-------------------------------------------------------------#

#connect to MySQL

mydb = mysql.connector.connect(
host="localhost",
user="root",
passwd="4655",
database="covid_19"
)

#check if connection is established
# if (mydb):
#     print("Connection Successful")
# else:
#     print("Connection Unsuccessful")


