import pandas as pd

df=pd.read_excel(r"C:\Users\nookaraju.c\Desktop\Tasks\7.6.2022\Task 6.xlsx")
df.columns=["Company_Code","Date","Price"]
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Month'] =  df['Date'].dt.month
df['Quarter'] =  df['Date'].dt.quarter
df["Month_3"] = df["Date"].dt.to_period(freq = '3M')

df['Week'] =  df['Date'].dt.isocalendar().week

dtd_data = df.copy()
dtd_data=dtd_data.sort_values(by=['Company_Code','Date']).reset_index(drop=True)
#Price Change
dtd_data["Price_Prev"]=dtd_data.groupby('Company_Code')['Price'].shift(1)
dtd_data["Return1"]=dtd_data['Price'] -dtd_data["Price_Prev"] 
dtd_pchange=dtd_data.groupby(['Company_Code']).tail(1)
#Pct Change
dtd_data['Return'] = dtd_data.groupby(['Company_Code'])['Price'].pct_change()
dtd_pct= dtd_data.groupby(['Company_Code']).tail(1)

dtd_pct=dtd_pct[['Company_Code','Price',"Return1",'Return']]
dtd_pct.columns=['Company_Code','CurrentPrice',"DailyChange","DailyPercentChange"]
#==========================================================================================
wtd_data = df.copy()
wtd_data=wtd_data.sort_values('Date',ascending=True).reset_index(drop=True)
#wtd_data=wtd_data.sort_values(by=['Company_Code','Date']).reset_index(drop=True)
wtd_data  = wtd_data.groupby(['Year','Month',"Week",'Company_Code']).tail(1)

#Price Change 
wtd_data["Price_Prev"]=wtd_data.groupby('Company_Code')['Price'].shift(1)
wtd_data["Return1"]=wtd_data['Price'] -wtd_data["Price_Prev"] 
wtd_pchange=wtd_data.groupby(['Company_Code']).tail(1)

#Pct Change
wtd_data['Return'] = wtd_data.groupby(['Company_Code'])['Price'].pct_change()
wtd_final= wtd_data.groupby(['Company_Code']).tail(1)

wtd_final=wtd_final[['Company_Code',"Return1",'Return']]
wtd_final.columns=['Company_Code',"WTD_price_change","WTD_price_change_percent"]

#==========================================================================================

mtd_data = df.copy()
mtd_data=mtd_data.sort_values('Date',ascending=True).reset_index(drop=True)

mtd_data  = mtd_data.groupby(['Year','Month','Company_Code']).tail(1)
#mtd_data=mtd_data.sort_values(by=['Company_Code','Date']).reset_index(drop=True)
#Price Change
mtd_data["Price_Prev"]=mtd_data.groupby('Company_Code')['Price'].shift(1)
mtd_data["Return1"]=mtd_data['Price'] -mtd_data["Price_Prev"] 
mtd_pchange=mtd_data.groupby(['Company_Code']).tail(1)
#Pct Change
mtd_data['Return'] = mtd_data.groupby(['Company_Code'])['Price'].pct_change()
mtd_final= mtd_data.groupby(['Company_Code']).tail(1)

mtd_final=mtd_final[['Company_Code',"Return1",'Return']]
mtd_final.columns=['Company_Code',"MTD_price_change","MTD_price_change_percent"]

#==========================================================================================

ytd_data = df.copy()
ytd_data=ytd_data.sort_values('Date',ascending=True).reset_index(drop=True)

ytd_data =  ytd_data.groupby(['Year','Company_Code']).tail(1)
#ytd_data=ytd_data.sort_values(by=['Company_Code','Date']).reset_index(drop=True)
#Price Change
ytd_data["Price_Prev"]=ytd_data.groupby('Company_Code')['Price'].shift(1)
ytd_data["Return1"]=ytd_data['Price'] -ytd_data["Price_Prev"] 
ytd_pchange=ytd_data.groupby(['Company_Code']).tail(1)
#Pct Change
ytd_data['Return'] = ytd_data.groupby(['Company_Code'])['Price'].pct_change()
ytd_final= ytd_data.groupby(['Company_Code']).tail(1)


ytd_final=ytd_final[['Company_Code',"Return1",'Return']]
ytd_final.columns=['Company_Code',"YTD_price_change","YTD_price_change_percent"]

#==========================================================================================
w5_td_data = df.copy()
w5_td_data=w5_td_data.sort_values(by=['Company_Code','Date']).reset_index(drop=True)

#Price Change

w5_td_data=w5_td_data.set_index('Date') 
w5_td_data["Price_Prev"]=w5_td_data.groupby('Company_Code')['Price'].shift(4)
w5_td_data["Return1"]=w5_td_data['Price'] -w5_td_data["Price_Prev"] 
w5_td_change=w5_td_data.groupby(['Company_Code']).tail(1)


#Pct Change

w5_td_data['Return'] = w5_td_data["Return1"]/w5_td_data["Price_Prev"]

w5_td_final= w5_td_data.groupby(['Company_Code']).tail(1)


w5_td_final=w5_td_final[['Company_Code',"Return1",'Return']]
w5_td_final.columns=['Company_Code',"WeeklyChange","WeeklyPercentChange"]


#============================================================================================

qtd_data = df.copy()
qtd_data=qtd_data.sort_values('Date',ascending=True).reset_index(drop=True)

qtd_data  = qtd_data.groupby(['Year','Quarter','Company_Code']).tail(1)
#mtd_data=mtd_data.sort_values(by=['Company_Code','Date']).reset_index(drop=True)
#Price Change
qtd_data["Price_Prev"]=qtd_data.groupby('Company_Code')['Price'].shift(1)
qtd_data["Return1"]=qtd_data['Price'] -qtd_data["Price_Prev"] 
qtd_pchange=qtd_data.groupby(['Company_Code']).tail(1)
#Pct Change
qtd_data['Return'] = qtd_data.groupby(['Company_Code'])['Price'].pct_change()
qtd_final= qtd_data.groupby(['Company_Code']).tail(1)


qtd_final=qtd_final[['Company_Code',"Return1",'Return']]
qtd_final.columns=['Company_Code',"QTD_price_change","QTD_price_change_percent"]

#============================================================================================

m3_td_data = df.copy()
m3_td_data=m3_td_data.sort_values('Date',ascending=True).reset_index(drop=True)
m3_td_data["Max_date"]=m3_td_data["Date"].max()
m3_td_data["Diff_days"]=(m3_td_data["Max_date"]- m3_td_data["Date"]).dt.days


new_df=m3_td_data[m3_td_data["Date"]==m3_td_data["Max_date"]][['Date', "Company_Code","Price"]]
new_df.columns=['Date', "Company_Code","Price_Prev"]

new_df_2=m3_td_data[m3_td_data["Diff_days"]>=31]
m3_td_data=new_df_2.groupby("Company_Code").tail(1)

final_m3_td_data=m3_td_data[['Company_Code', 'Date', 'Price', 'Year', 'Month', 'Quarter', 'Month_3',
       'Week', 'Max_date', 'Diff_days']].merge(new_df[["Company_Code","Price_Prev"]],on="Company_Code",how="left")

#Price Change
final_m3_td_data["Return1"]=final_m3_td_data['Price'] -final_m3_td_data["Price_Prev"] 
final_m3_td_pchange=final_m3_td_data.groupby(['Company_Code']).tail(1)
#Pct Change
#final_m3_td_data['Return'] = final_m3_td_data.groupby(['Company_Code'])['Price_Prev'].pct_change()
final_m3_td_data['Return'] = (final_m3_td_data["Price_Prev"]/final_m3_td_data['Price'])-1
final_m3_td_final= final_m3_td_data.groupby(['Company_Code']).tail(1)



final_m3_td_final=final_m3_td_final[['Company_Code',"Return1",'Return']]
final_m3_td_final.columns=['Company_Code',"MonthlyPriceChange","MonthlyPriceChangePercent"]

#============================================================================================

m9_td_data = df.copy()
m9_td_data=m9_td_data.sort_values('Date',ascending=True).reset_index(drop=True)
m9_td_data["Max_date"]=m9_td_data["Date"].max()
m9_td_data["Diff_days"]=(m9_td_data["Max_date"]- m9_td_data["Date"]).dt.days


new_df=m9_td_data[m9_td_data["Date"]==m9_td_data["Max_date"]][['Date', "Company_Code","Price"]]
new_df.columns=['Date', "Company_Code","Price_Prev"]

new_df_2=m9_td_data[m9_td_data["Diff_days"]>=90]
m9_td_data=new_df_2.groupby("Company_Code").tail(1)

final_m9_td_data=m9_td_data[['Company_Code', 'Date', 'Price', 'Year', 'Month', 'Quarter', 'Month_3',
       'Week', 'Max_date', 'Diff_days']].merge(new_df[["Company_Code","Price_Prev"]],on="Company_Code",how="left")

#Price Change
final_m9_td_data["Return1"]=final_m9_td_data["Price_Prev"]  - final_m9_td_data['Price'] 
final_m9_td_pchange=final_m9_td_data.groupby(['Company_Code']).tail(1)
#Pct Change
#final_m3_td_data['Return'] = final_m3_td_data.groupby(['Company_Code'])['Price_Prev'].pct_change()
final_m9_td_data['Return'] = (final_m9_td_data["Price_Prev"]/final_m9_td_data['Price'])-1
final_m9_td_final= final_m9_td_data.groupby(['Company_Code']).tail(1)


final_m9_td_final=final_m9_td_final[['Company_Code',"Return1",'Return']]
final_m9_td_final.columns=['Company_Code',"3M_price_change","3M_price_change_percent"]
#============================================================================================

m18_td_data = df.copy()
m18_td_data=m18_td_data.sort_values('Date',ascending=True).reset_index(drop=True)
m18_td_data["Max_date"]=m18_td_data["Date"].max()
m18_td_data["Diff_days"]=(m18_td_data["Max_date"]- m18_td_data["Date"]).dt.days


new_df=m18_td_data[m18_td_data["Date"]==m18_td_data["Max_date"]][['Date', "Company_Code","Price"]]
new_df.columns=['Date', "Company_Code","Price_Prev"]

new_df_2=m18_td_data[m18_td_data["Diff_days"]>=180]
m18_td_data=new_df_2.groupby("Company_Code").tail(1)

final_m18_td_data=m18_td_data[['Company_Code', 'Date', 'Price', 'Year', 'Month', 'Quarter', 'Month_3',
       'Week', 'Max_date', 'Diff_days']].merge(new_df[["Company_Code","Price_Prev"]],on="Company_Code",how="left")

#Price Change
final_m18_td_data["Return1"]=final_m18_td_data["Price_Prev"] - final_m18_td_data['Price'] 
final_m18_td_pchange=final_m18_td_data.groupby(['Company_Code']).tail(1)
#Pct Change
#final_m3_td_data['Return'] = final_m3_td_data.groupby(['Company_Code'])['Price_Prev'].pct_change()
final_m18_td_data['Return'] = (final_m18_td_data["Price_Prev"]/final_m18_td_data['Price'])-1
final_m18_td_final= final_m18_td_data.groupby(['Company_Code']).tail(1)



final_m18_td_final=final_m18_td_final[['Company_Code',"Return1",'Return']]
final_m18_td_final.columns=['Company_Code',"6M_price_change","6M_price_change_percent"]

#============================================================================================

m365_td_data = df.copy()
m365_td_data=m365_td_data.sort_values('Date',ascending=True).reset_index(drop=True)
m365_td_data["Max_date"]=m365_td_data["Date"].max()
m365_td_data["Diff_days"]=(m365_td_data["Max_date"]- m365_td_data["Date"]).dt.days


new_df=m365_td_data[m365_td_data["Date"]==m365_td_data["Max_date"]][['Date', "Company_Code","Price"]]
new_df.columns=['Date', "Company_Code","Price_Prev"]

new_df_2=m365_td_data[m365_td_data["Diff_days"]>=365]
m365_td_data=new_df_2.groupby("Company_Code").tail(1)

final_m365_td_data=m365_td_data[['Company_Code', 'Date', 'Price', 'Year', 'Month', 'Quarter', 'Month_3',
       'Week', 'Max_date', 'Diff_days']].merge(new_df[["Company_Code","Price_Prev"]],on="Company_Code",how="left")

#Price Change
final_m365_td_data["Return1"]=final_m365_td_data["Price_Prev"] - final_m365_td_data['Price'] 
final_m365_td_pchange=final_m365_td_data.groupby(['Company_Code']).tail(1)
#Pct Change
#final_m3_td_data['Return'] = final_m3_td_data.groupby(['Company_Code'])['Price_Prev'].pct_change()
final_m365_td_data['Return'] = (final_m365_td_data["Price_Prev"]/final_m365_td_data['Price'])-1
final_m365_td_final= final_m365_td_data.groupby(['Company_Code']).tail(1)

final_m365_td_final=final_m365_td_final[['Company_Code',"Return1",'Return']]
final_m365_td_final.columns=['Company_Code',"yearly_price_change","yearly_price_change_percent"]


#==============Merging==============================================================================

final_output=dtd_pct.merge(wtd_final,on='Company_Code',how ='left').merge(w5_td_final,on='Company_Code',how ='left').merge(mtd_final,on='Company_Code',how ='left').merge(final_m3_td_final,on='Company_Code',how ='left').merge(final_m9_td_final,on='Company_Code',how ='left').merge(final_m18_td_final,on='Company_Code',how ='left').merge(qtd_final,on='Company_Code',how ='left').merge(ytd_final,on='Company_Code',how ='left').merge(final_m365_td_final,on='Company_Code',how ='left')
final_output.to_excel("C:\\Users\\nookaraju.c\\Desktop\\Tasks\\7.6.2022\\Final_Output.xlsx")





















