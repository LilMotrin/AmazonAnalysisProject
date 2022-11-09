import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#reads csv file
df = pd.read_csv('amazon-orders.csv')
df.head()
# Gives Shape of Data DataFrame
df.shape
#Cleans up NaN in Table
df = df.fillna(0)
df.head()
#Series.str.replace('Characters to Replace', 'New Characters') to clean up Numbers
#Check For Column Name
print(df.columns.tolist())
df["Item Total"] = df['Item Total'].str.replace('$', '').astype(float)
df.head()
df["Item Total"].sum()
#Test Check
(df["Item Total"].sum())
print("Item Total Sum: " + str(df["Item Total"].sum()))
#All Stats of Item Purchases
df["Item Total"].mean()
df["Item Total"].median()
df["Item Total"].max()
df["Item Total"].min()
#Check Tax Charged :(
df["Item Subtotal Tax"] = df["Item Subtotal Tax"].str.replace('$', '').astype(float)
df.head()
df["Item Subtotal Tax"].sum()
print("Tax Charged Sum: " + str(df["Item Subtotal Tax"].sum()))
#Percentage Charged as Tax
df["Item Subtotal Tax"].sum() / df["Item Total"].sum()
print("Percentage of Total Charged as Tax " + str(df["Item Subtotal Tax"].sum() / df["Item Total"].sum()))
#Checking Total Spent by Date
df["Order Date"] = pd.to_datetime(df["Order Date"])
df.head()
#Plotting Order Dates on Graph
#df.plot.bar(x='Order Date', y='Item Total', rot=90, figsize=(20,10))
plt.show()
#Grouping Orders by Day
daily_orders = df.groupby('Order Date').sum()['Item Total']
daily_orders.head()
print(daily_orders.head)
#Plotting Daily Orders Graph
daily_orders.plot.bar(figsize=(20, 10), color='#75D232')
plt.show()
