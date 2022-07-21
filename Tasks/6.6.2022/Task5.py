import pandas as pd
from datetime import datetime as dt



input_data=pd.read_excel(r"C:\Users\nookaraju.c\Downloads\Task5.xlsx")
input_data=input_data[['Date', 'Index Name', 'Price']]
input_data.columns=['Date','FS_Ticker','Price']
input_data['Date'] = pd.to_datetime(input_data['Date'])
input_data['Year'] = input_data['Date'].dt.year
input_data['Month'] =  input_data['Date'].dt.month
mtd_data = input_data.copy()
mtd_data  = mtd_data.groupby(['Year','Month','FS_Ticker']).tail(1)
mtd_data=mtd_data.sort_values(by=['FS_Ticker','Date']).reset_index(drop=True)
mtd_data['Return'] = mtd_data.groupby(['FS_Ticker'])['Price'].pct_change()
mtd_data['Return']=mtd_data['Return']*100

ytd_data = input_data.copy()
ytd_data =  ytd_data.groupby(['FS_Ticker','Year']).tail(1)
ytd_data=ytd_data.sort_values(by=['FS_Ticker','Date']).reset_index(drop=True)
ytd_data['Return'] = ytd_data.groupby(['FS_Ticker'])['Price'].pct_change()
ytd_data['Return']=ytd_data['Return']*100
ytd_data=ytd_data.groupby(['FS_Ticker','Year']).tail(1).reset_index(drop=True)


a=ytd_data.pivot(index="FS_Ticker",columns="Year",values="Return")
a.columns=["Y","2021","YTD"]
a=a[["YTD","2021"]]


mtd_data["Month"]=mtd_data["Date"].dt.strftime("%b -%y")
b=mtd_data.pivot_table(index="FS_Ticker",columns="Month",values="Return")

#b.columns=["Jan-22","Feb-22","Mar-22","Apr-22","May-22","Jun-22","Dec-22"]

#b=b[["Jun-22","May-22","Apr-22","Mar-22","Feb-22","Jan-22"]]

#now.strftime("%b %-y")

final=pd.concat([b, a], axis=1, join='inner')
print(final)

