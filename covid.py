import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkinter import *


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

# print(tonnes_df)          #for testing 
# print(dollar_df)

tonnes_df_first_sql= grouped_first_df[grouped_first_df['Measure'] == 'Tonnes']
dollar_df_first_sql= grouped_first_df[grouped_first_df['Measure'] == '$']

#parse dataframes to lists
tonnes_df_list = tonnes_df['Value'].tolist()
dollar_df_list = dollar_df['Value'].tolist()

# print (tonnes_df_list)
# print (dollar_df_list)

################### plot $ and Tonnes value per month per year ###########################################

def plot_dollars_1():
    values = dollar_df['Value']
    years = dollar_df['Year']
    months = dollar_df['Month']   #???
    fig, ax = plt.subplots()

    labels = [f"{m}-{y}" for m, y in zip(months, years)]
    ax.set_xticks(np.arange(len(labels)))
    ax.set_xticklabels(labels)

    ax.bar(np.arange(len(values)), values)

    ax.set_xlabel('Month-Year')
    ax.set_ylabel('Dollars')
    ax.set_title('Dollars per Month')
    plt.xticks(rotation=90)
    plt.show()

def plot_tonnes_1():
    values = tonnes_df['Value']
    years = tonnes_df['Year']
    months = tonnes_df['Month']   #???
    fig, ax = plt.subplots()

    labels = [f"{m}-{y}" for m, y in zip(months, years)]
    ax.set_xticks(np.arange(len(labels)))
    ax.set_xticklabels(labels)

    ax.bar(np.arange(len(values)), values, color='orange')
    ax.set_xlabel('Month-Year')
    ax.set_ylabel('Tonnes')
    ax.set_title('Tonnes per Month')
    plt.xticks(rotation=90)
    plt.show()

# plot_dollars_1()
# plot_tonnes_1()

#------------------------------------- ER2 ------------------------------------------------------------#

#Συνολική παρουσίαση του τζίρου (στήλη value) ανά χώρα (στις αντίστοιχες μονάδες μέτρησης).  

grouped_second_df=df.groupby(['Country','Measure'])[["Value"]].sum().reset_index()
# print(grouped_second_df)  

# i need to divide the dataframe into 2 dataframes, one for $ and one for tonnes
tonnes_df_2 = grouped_second_df[grouped_second_df['Measure'] == 'Tonnes']
dollar_df_2 = grouped_second_df[grouped_second_df['Measure'] == '$']

print(tonnes_df_2)
print(dollar_df_2)

tonnes_df_second_sql= grouped_second_df[grouped_second_df['Measure'] == 'Tonnes']
dollar_df_second_sql= grouped_second_df[grouped_second_df['Measure'] == '$']

# print(tonnes_df_second_sql)
# print(dollar_df_second_sql)

#parse dataframes to lists
country_tonnes_df_list = tonnes_df['Value'].tolist()
country_dollar_df_list = dollar_df['Value'].tolist()

# print (country_tonnes_df_list)
# print (country_dollar_df_list)

#plot $ and Tonnes value per country ###########################################

def plot_dollars_2():
    countries = dollar_df_2['Country']
    values = dollar_df_2['Value']

    fig, ax = plt.subplots()

    labels = [f"{c}" for c in countries]
    ax.set_xticks(np.arange(len(labels)))
    ax.set_xticklabels(labels)

    ax.bar(np.arange(len(values)), values)

    ax.set_xlabel('Country')
    ax.set_ylabel('Dollars')
    ax.set_title('Dollars per Country')
    plt.xticks(rotation=90)
    plt.show()

def plot_tonnes_2():
    countries = tonnes_df_2['Country']
    values = tonnes_df_2['Value']

    fig, ax = plt.subplots()

    labels = [f"{c}" for c in countries]
    ax.set_xticks(np.arange(len(labels)))
    ax.set_xticklabels(labels)

    ax.bar(np.arange(len(values)), values, color='orange')

    ax.set_xlabel('Country')
    ax.set_ylabel('Tonnes')
    ax.set_title('Tonnes per Country')
    plt.xticks(rotation=90)
    plt.show()

# plot_dollars_2()
# plot_tonnes_2()

#------------------------------------- ER3 ------------------------------------------------------------#
# Συνολική παρουσίαση του τζίρου (στήλη value) για κάθε μέσο μεταφοράς (στις αντίστοιχες μονάδες μέτρησης)

grouped_third_df=df.groupby(['Transport_Mode','Measure'])[["Value"]].sum().reset_index()
# print(grouped_third_df)

# i need to divide the dataframe into 2 dataframes, one for $ and one for tonnes
transport_tonnes_df = grouped_third_df[grouped_third_df['Measure'] == 'Tonnes']
transport_dollar_df = grouped_third_df[grouped_third_df['Measure'] == '$']

# print(transport_tonnes_df)
# print(transport_dollar_df)

transport_tonnes_df_third_sql= grouped_third_df[grouped_third_df['Measure'] == 'Tonnes']
transport_dollar_df_third_sql= grouped_third_df[grouped_third_df['Measure'] == '$']


#plot $ and Tonnes value per transport ###########################################

def plot_dollars_3():
    transports = transport_dollar_df['Transport_Mode']
    values = transport_dollar_df['Value']

    fig, ax = plt.subplots()

    labels = [f"{t}" for t in transports]
    ax.set_xticks(np.arange(len(labels)))
    ax.set_xticklabels(labels)

    ax.bar(np.arange(len(values)), values)

    ax.set_xlabel('Transport')
    ax.set_ylabel('Dollars')
    ax.set_title('Dollars per Transport')
    plt.xticks(rotation=90)
    plt.show()

def plot_tonnes_3():
    transports = transport_tonnes_df['Transport_Mode']
    values = transport_tonnes_df['Value']

    fig, ax = plt.subplots()

    labels = [f"{t}" for t in transports]
    ax.set_xticks(np.arange(len(labels)))
    ax.set_xticklabels(labels)

    ax.bar(np.arange(len(values)), values, color='orange')

    ax.set_xlabel('Transport')
    ax.set_ylabel('Tonnes')
    ax.set_title('Tonnes per Transport')
    plt.xticks(rotation=90)
    plt.show()

# plot_dollars_3()
# plot_tonnes_3()


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

weekday_tonnes_df_sql= grouped_fourth_df[grouped_fourth_df['Measure'] == 'Tonnes']
weekday_dollar_df_sql= grouped_fourth_df[grouped_fourth_df['Measure'] == '$']

# print(weekday_tonnes_df_sql)
# print(weekday_dollar_df_sql)

#plot $ and Tonnes value per weekday ###########################################

def plot_dollars_4():
    weekdays = weekday_dollar_df['Weekday']
    values = weekday_dollar_df['Value']

    fig, ax = plt.subplots()

    labels = [f"{w}" for w in weekdays]
    ax.set_xticks(np.arange(len(labels)))
    ax.set_xticklabels(labels)

    ax.bar(np.arange(len(values)), values)

    ax.set_xlabel('Weekday')
    ax.set_ylabel('Dollars')
    ax.set_title('Dollars per Weekday')
    plt.xticks(rotation=90)
    plt.show()

def plot_tonnes_4():
    weekdays = weekday_tonnes_df['Weekday']
    values = weekday_tonnes_df['Value']

    fig, ax = plt.subplots()

    labels = [f"{w}" for w in weekdays]
    ax.set_xticks(np.arange(len(labels)))
    ax.set_xticklabels(labels)

    ax.bar(np.arange(len(values)), values, color='orange')

    ax.set_xlabel('Weekday')
    ax.set_ylabel('Tonnes')
    ax.set_title('Tonnes per Weekday')
    plt.xticks(rotation=90)
    plt.show()

# plot_dollars_4()
# plot_tonnes_4()

#------------------------------------- ER5 ------------------------------------------------------------#
#Συνολική παρουσίαση του τζίρου (στήλη value) για κάθε κατηγορία εμπορεύματος (στις αντίστοιχες μονάδες μέτρησης)

grouped_fifth_df=df.groupby(['Commodity','Measure'])[["Value"]].sum().reset_index()
# print(grouped_fifth_df)

commodity_tonnes_df = grouped_fifth_df[grouped_fifth_df['Measure'] == 'Tonnes']
commodity_dollar_df = grouped_fifth_df[grouped_fifth_df['Measure'] == '$']

commodity_tonnes_df_sql= grouped_fifth_df[grouped_fifth_df['Measure'] == 'Tonnes']
commodity_dollar_df_sql= grouped_fifth_df[grouped_fifth_df['Measure'] == '$']

# print(commodity_tonnes_df_sql)
# print(commodity_dollar_df_sql)

# lists
commodity_tonnes_df_list = commodity_tonnes_df['Value'].tolist()
commodity_dollar_df_list = commodity_dollar_df['Value'].tolist()

#plot $ and Tonnes value per commodity ###########################################

def plot_dollars_5():
    commodities = commodity_dollar_df['Commodity']
    values = commodity_dollar_df['Value']

    fig, ax = plt.subplots()

    labels = [f"{c}" for c in commodities]
    ax.set_xticks(np.arange(len(labels)))
    ax.set_xticklabels(labels)

    ax.bar(np.arange(len(values)), values)

    ax.set_xlabel('Commodity')
    ax.set_ylabel('Dollars')
    ax.set_title('Dollars per Commodity')
    plt.xticks(rotation=90)
    plt.show()

    fig, ax = plt.subplots()
    ax.pie(commodity_dollar_df_list, labels=commodity_dollar_df['Commodity'], autopct='%1.1f%%', shadow=True, startangle=90)
    for text in ax.texts:
        text.set_size(6)
        text.set_color(ax.patches[ax.texts.index(text)].get_facecolor())
    ax.axis('equal')  
    ax.set_title('Dollars per Commodity')
    plt.show()

#define plot_tonnes_5() (show both bar and pie chart)

def plot_tonnes_5():
    commodities = commodity_tonnes_df['Commodity']
    values = commodity_tonnes_df['Value']

    fig, ax = plt.subplots()

    labels = [f"{c}" for c in commodities]
    ax.set_xticks(np.arange(len(labels)))
    ax.set_xticklabels(labels)

    ax.bar(np.arange(len(values)), values, color='orange')

    ax.set_xlabel('Commodity')
    ax.set_ylabel('Tonnes')
    ax.set_title('Tonnes per Commodity')
    plt.xticks(rotation=90)
    plt.show()

    fig, ax = plt.subplots()
    ax.pie(commodity_tonnes_df_list, labels=commodity_tonnes_df['Commodity'], autopct='%1.1f%%', shadow=True, startangle=90)
    for text in ax.texts:
        text.set_size(6)
        text.set_color(ax.patches[ax.texts.index(text)].get_facecolor())
    ax.axis('equal')  
    ax.set_title('Tonnes per Commodity')
    plt.show()

# plot_dollars_5()
# plot_tonnes_5()


#------------------------------------- ER6 ------------------------------------------------------------#
#Παρουσίαση των 5 μηνών με το μεγαλύτερο τζίρο, ανεξαρτήτως μέσου μεταφοράς και είδους ανακυκλώσιμων ειδών

grouped_sixth_df=df.groupby(['Year','Month','Measure'])[["Value"]].sum().reset_index().sort_values(by=['Value'], ascending=False).head(5)   #both $ and tonnes
# print(grouped_sixth_df)

grouped_sixth_df_sql=df.groupby(['Year','Month','Measure'])[["Value"]].sum().reset_index().sort_values(by=['Value'], ascending=False).head(5)   

# lists
grouped_sixth_df_list = grouped_sixth_df['Value'].tolist()

def plot_values_6():
    months = grouped_sixth_df['Month']
    values = grouped_sixth_df['Value']

    fig, ax = plt.subplots()

    labels = [f"{m}" for m in months]
    ax.set_xticks(np.arange(len(labels)))
    ax.set_xticklabels(labels)

    ax.bar(np.arange(len(values)), values, color='orange')

    ax.set_xlabel('Month')
    ax.set_ylabel('Value($ and Tonnes))')
    ax.set_title('Value per Month (Top 5)')
    plt.xticks(rotation=90)
    plt.show()

# plot_values_6()

#------------------------------------- ER7 ------------------------------------------------------------#
#Παρουσίαση των 5 κατηγοριών εμπορευμάτων με το μεγαλύτερο τζίρο, για κάθε χώρα
#Presentation of the 5 categories of goods with the highest turnover, for each country(sos)

# Group the data by 'Country' and 'Commodity' and get the sum of the 'Value' column
grouped_data2 = df.groupby(['Country', 'Commodity'])[['Value']].sum().reset_index()
# print(grouped_data2)

#fir eacg country get the top 5 categories
grouped_data2 = grouped_data2.groupby('Country').head(5)
print(grouped_data2)

seventh_df_sql=grouped_data2.groupby('Country').head(5)
# print(seventh_df_sql)

def plot_values_7():
    num_countries = len(grouped_data2['Country'].unique())
    num_plots_per_row = 2  # Number of plots to display in each row

    num_rows = (num_countries + num_plots_per_row - 1) // num_plots_per_row  # Calculate the number of rows needed

    fig, axes = plt.subplots(num_rows, num_plots_per_row, figsize=(9, 3*num_rows))
    fig.tight_layout(pad=10.0)  # Adjust the spacing between subplots

    for i, country in enumerate(grouped_data2['Country'].unique()):
        country_data = grouped_data2[grouped_data2['Country'] == country]
        commodities = country_data['Commodity']
        values = country_data['Value']

        ax = axes[i // num_plots_per_row, i % num_plots_per_row]

        labels = [f"{c}" for c in commodities]
        ax.barh(labels, values, color='orange')

        ax.set_xlabel('Value ($ and Tonnes)', fontsize=8)
        ax.set_ylabel('Commodity', fontsize=8)
        ax.set_title(f'Value per Commodity for {country}', fontsize=8)
        ax.invert_yaxis()  # commodities from top to bottom
        ax.tick_params(axis='y', labelsize=6)  

    plt.show()

# plot_values_7()

#------------------------------------- ER8 ------------------------------------------------------------#
# Παρουσίαση της ημέρας με το μεγαλύτερο τζίρο, για κάθε κατηγορία εμπορεύματος

# Group the data by 'Commodity' and get the sum of the 'Value' column

grouped_data = df.groupby(['Commodity'])[['Value']].sum().reset_index()
# The above code is printing the value of a variable named "grouped_data" in Python.
# print(grouped_data)

#get the day with the highest value for each commodity 
grouped_data = df.groupby(['Commodity','Date'])[['Value']].sum().reset_index().sort_values(by=['Value'], ascending=False)
# print(grouped_data)

#get the day with the highest value for each commodity
grouped_data = grouped_data.groupby('Commodity').head(1)
# print(grouped_data)

eighth_df_sql=grouped_data.groupby('Commodity').head(1)
# print(eigth_df_sql)

#define plot_values_8 (add the dates next to the commodities)
def plot_values_8():
    commodities = grouped_data['Commodity']
    values = grouped_data['Value']
    dates = grouped_data['Date']

    fig, ax = plt.subplots()

    labels = [f"{c}\n{d}" for c, d in zip(commodities, dates)]  # Concatenate the commodity and date
    ax.set_xticks(np.arange(len(labels)))
    ax.set_xticklabels(labels)

    ax.bar(np.arange(len(values)), values, color='orange')

    ax.set_xlabel('Commodity\nDate')  # Update the x-axis label
    ax.set_ylabel('Value ($ and Tonnes)')
    ax.set_title('Value per Commodity')
    plt.xticks(rotation=90)
    plt.show()


# plot_values_8()    

#-------------------------------------------------------------MySQL Connection-------------------------------------------------------------#

#connect to MySQL

mydb = mysql.connector.connect(
host="localhost",
user="root",
passwd="4655",
database="covid_data"
)

#check if connection is established
# if (mydb):
#     print("Connection Successful")
# else:
#     print("Connection Unsuccessful")

mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE covid_data")

#----------------------------------------------------- SQL 1 ---------------------------------------------------------------------#

# first question table (value per month for both $ and tonnes)
# mycursor.execute("DROP TABLE IF EXISTS value_per_month_tonnes")
# mycursor.execute("CREATE TABLE if not exists value_per_month_tonnes (Year INT, Month INT, Measure TEXT, Value INT)")

# #parse tonnes_df_first_sql to the table
# for row in tonnes_df_first_sql.itertuples():
#     sql = "INSERT INTO value_per_month_tonnes (Year, Month, Measure, Value) VALUES (%s, %s, %s, %s)"
#     val = (row.Year, row.Month, row.Measure, row.Value)
#     mycursor.execute(sql, val)
#     mydb.commit()

# mycursor.execute("DROP TABLE IF EXISTS value_per_month_dollars")
# mycursor.execute("CREATE TABLE if not exists value_per_month_dollars (Year INT, Month INT, Measure TEXT, Value BIGINT)")

# # parse dollar_df_first_sql to the table
# for row in dollar_df_first_sql.itertuples():
#     sql = "INSERT INTO value_per_month_dollars (Year, Month, Measure, Value) VALUES (%s, %s, %s, %s)"
#     val = (row.Year, row.Month, row.Measure, row.Value)
#     mycursor.execute(sql, val)
#     mydb.commit()

#------------------------------------------------------------- SQL 2 -------------------------------------------------------------#

# mycursor.execute("DROP TABLE IF EXISTS value_per_country_tonnes")
# mycursor.execute("CREATE TABLE if not exists value_per_country_tonnes (Country TEXT, Measure TEXT, Value BIGINT)")

# # parse tonnes_df_second_sql to the table
# for row in tonnes_df_second_sql.itertuples():
#     sql = "INSERT INTO value_per_country_tonnes (Country, Measure, Value) VALUES (%s, %s, %s)"
#     val = (row.Country, row.Measure, row.Value)
#     mycursor.execute(sql, val)
#     mydb.commit()


# mycursor.execute("DROP TABLE IF EXISTS value_per_country_dollars")
# mycursor.execute("CREATE TABLE if not exists value_per_country_dollars (Country TEXT, Measure TEXT, Value BIGINT)")

# # parse dollar_df_second_sql to the table
# for row in dollar_df_second_sql.itertuples():
#     sql = "INSERT INTO value_per_country_dollars (Country, Measure, Value) VALUES (%s, %s, %s)"
#     val = (row.Country, row.Measure, row.Value)
#     mycursor.execute(sql, val)
#     mydb.commit()

#------------------------------------------------------------- SQL 3 -------------------------------------------------------------#

# mycursor.execute("DROP TABLE IF EXISTS value_per_transport_tonnes")
# mycursor.execute("CREATE TABLE if not exists value_per_transport_tonnes (Transport TEXT, Measure TEXT, Value BIGINT)")

# # parse transport_tonnes_df_third_sql
# for row in transport_tonnes_df_third_sql.itertuples():
#     sql = "INSERT INTO value_per_transport_tonnes (Transport, Measure, Value) VALUES (%s, %s, %s)"
#     val = (row.Transport_Mode, row.Measure, row.Value)
#     mycursor.execute(sql, val)
#     mydb.commit()

# mycursor.execute("DROP TABLE IF EXISTS value_per_transport_dollars")
# mycursor.execute("CREATE TABLE if not exists value_per_transport_dollars (Transport TEXT, Measure TEXT, Value BIGINT)")

# # parse transport_dollars_df_third_sql
# for row in transport_dollar_df_third_sql.itertuples():
#     sql = "INSERT INTO value_per_transport_dollars (Transport, Measure, Value) VALUES (%s, %s, %s)"
#     val = (row.Transport_Mode, row.Measure, row.Value)
#     mycursor.execute(sql, val)
#     mydb.commit()

#------------------------------------------------------------- SQL 4 -------------------------------------------------------------#

# mycursor.execute("DROP TABLE IF EXISTS value_per_weekday_tonnes")
# mycursor.execute("CREATE TABLE if not exists value_per_weekday_tonnes (Weekday TEXT, Measure TEXT, Value BIGINT)")

# # parse weekday_tonnes_df_sql
# for row in weekday_tonnes_df_sql.itertuples():
#     sql = "INSERT INTO value_per_weekday_tonnes (Weekday, Measure, Value) VALUES (%s, %s, %s)"
#     val = (row.Weekday, row.Measure, row.Value)
#     mycursor.execute(sql, val)
#     mydb.commit()

# mycursor.execute("DROP TABLE IF EXISTS value_per_weekday_dollars")
# mycursor.execute("CREATE TABLE if not exists value_per_weekday_dollars (Weekday TEXT, Measure TEXT, Value BIGINT)")

# # parse weekday_dollars_df_sql
# for row in weekday_dollar_df_sql.itertuples():
#     sql = "INSERT INTO value_per_weekday_dollars (Weekday, Measure, Value) VALUES (%s, %s, %s)"
#     val = (row.Weekday, row.Measure, row.Value)
#     mycursor.execute(sql, val)
#     mydb.commit()

#------------------------------------------------------------- SQL 5 -------------------------------------------------------------#

# mycursor.execute("DROP TABLE IF EXISTS value_per_commodity_tonnes")
# mycursor.execute("CREATE TABLE if not exists value_per_commodity_tonnes (Commodity TEXT, Measure TEXT, Value BIGINT)")

# # parse commodity_tonnes_df_sql
# for row in commodity_tonnes_df_sql.itertuples():
#     sql = "INSERT INTO value_per_commodity_tonnes (Commodity, Measure, Value) VALUES (%s, %s, %s)"
#     val = (row.Commodity, row.Measure, row.Value)
#     mycursor.execute(sql, val)
#     mydb.commit()

# mycursor.execute("DROP TABLE IF EXISTS value_per_commodity_dollars")
# mycursor.execute("CREATE TABLE if not exists value_per_commodity_dollars (Commodity TEXT, Measure TEXT, Value BIGINT)")

# # parse commodity_dollar_df_sql
# for row in commodity_dollar_df_sql.itertuples():
#     sql = "INSERT INTO value_per_commodity_dollars (Commodity, Measure, Value) VALUES (%s, %s, %s)"
#     val = (row.Commodity, row.Measure, row.Value)
#     mycursor.execute(sql, val)
#     mydb.commit()

#------------------------------------------------------------- SQL 6 -------------------------------------------------------------#

# mycursor.execute("DROP TABLE IF EXISTS value_per_month_top5")
# mycursor.execute("CREATE TABLE if not exists value_per_month_top5 (Year INT, Month INT, Measure TEXT, Value BIGINT)")

# # parse grouped_sixth_df_sql
# for row in grouped_sixth_df_sql.itertuples():
#     sql = "INSERT INTO value_per_month_top5 (Year, Month, Measure, Value) VALUES (%s, %s, %s, %s)"
#     val = (row.Year, row.Month, row.Measure, row.Value)
#     mycursor.execute(sql, val)
#     mydb.commit()

#------------------------------------------------------------- SQL 7 -------------------------------------------------------------#

# mycursor.execute("DROP TABLE IF EXISTS top5_categories_per_country")
# mycursor.execute("CREATE TABLE if not exists top5_categories_per_country (Country TEXT, Commodity TEXT, Value BIGINT)")

# # parse seventh_df_sql
# for row in seventh_df_sql.itertuples():
#     sql = "INSERT INTO top5_categories_per_country (Country, Commodity, Value) VALUES (%s, %s, %s)"
#     val = (row.Country, row.Commodity, row.Value)
#     mycursor.execute(sql, val)
#     mydb.commit()

#------------------------------------------------------------- SQL 8 -------------------------------------------------------------#

# mycursor.execute("DROP TABLE IF EXISTS best_day_per_commodity")
# mycursor.execute("CREATE TABLE if not exists best_day_per_commodity (Commodity TEXT, Date TEXT, Value BIGINT)")

# # parse eighth_df_sql
# for row in eighth_df_sql.itertuples():
#     sql = "INSERT INTO best_day_per_commodity (Commodity, Date, Value) VALUES (%s, %s, %s)"
#     val = (row.Commodity, row.Date, row.Value)
#     mycursor.execute(sql, val)
#     mydb.commit()



#---------------------- GUI -----------------------------------------------------------------------------------------------------------------------------------#

# Create the main window
root = Tk()
root.title("Covid_19 Data Analysis")
root.geometry("500x500")
root.configure(background='white')

# Calculate the center position of the window
window_width = root.winfo_reqwidth()
window_height = root.winfo_reqheight()
position_right = int(root.winfo_screenwidth() / 2 - window_width / 2)
position_down = int(root.winfo_screenheight() / 2 - window_height / 2)

# Set the window position
root.geometry("+{}+{}".format(position_right, position_down))

# Create a label
label_text = "Choose a plot to show:"
label = ttk.Label(root, text=label_text,background='purple', foreground='white', font=("Times New Roman", 16))
label.pack(pady=20)

# Create a combobox
choose_results = ttk.Combobox(root, width=35)
choose_results['values'] = (
    '1. Value per Month (Tonnes & Dollars)',
    '2. Value per Country (Tonnes & Dollars)',
    '3. Value per Transport Mode (Tonnes & Dollars)',
    '4. Value per Weekday (Tonnes & Dollars)',
    '5. Value per Commodity (Tonnes & Dollars)',
    '6. Top 5 Months with Highest Value',
    '7. Top 5 Categories per Country',
    '8. Day of Highest Value per Commodity'
)
choose_results.pack(pady=10)

# Disable text editing in the combobox
choose_results.configure(state="readonly")

# Create a button
def show_results():
    selected_value = choose_results.get()
    # Call your already defined functions based on the selected value
    if selected_value == '1. Value per Month (Tonnes & Dollars)':
        plot_dollars_1()
        plot_tonnes_1()
        pass
    elif selected_value == '2. Value per Country (Tonnes & Dollars)':
        plot_dollars_2()
        plot_tonnes_2()
        pass
    elif selected_value == '3. Value per Transport Mode (Tonnes & Dollars)':
        plot_dollars_3()
        plot_tonnes_3()
        pass
    elif selected_value == '4. Value per Weekday (Tonnes & Dollars)':
        plot_dollars_4()
        plot_tonnes_4()
        pass
    elif selected_value == '5. Value per Commodity (Tonnes & Dollars)':
        plot_dollars_5()
        plot_tonnes_5()
        pass
    elif selected_value == '6. Top 5 Months with Highest Value':
        plot_values_6()
        pass
    elif selected_value == '7. Top 5 Categories per Country':
        plot_values_7()
        pass
    elif selected_value == '8. Day of Highest Value per Commodity':
        plot_values_8()   
        pass

button = ttk.Button(root, text="Show me the results", command=show_results)
button.pack(pady=10)

root.mainloop()