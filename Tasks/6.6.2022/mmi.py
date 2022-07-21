import pandas as pd
df=pd.read_excel("C:\\Users\\nookaraju.c\\Downloads\\Task5.xlsx")
df=df[["Date","Index Name","Price"]]

Y2021={}

#print(str(df["Date"].max())[0:11])

#df.loc[df.Unit_Price >= 1000,'Product_Name'].tolist()
#print((df.loc[df.Date=="2021-12-31"])["Index Name"].values)

#df1=(df.loc[df.Date=="2021-12-31"]).groupby("Index Name")

#print(df1)

#df2=df1.loc[df1.Index Name=="4766.1802"]

#print(df.groupby("Index Name",as_index =False)[["Date","Index Name","Price"]])



#df1=df.groupby(pd.Grouper(key='Date', freq='Y')).max()
#print(df1)

#df1=df.groupby(["Date","Index Name"]).first()
#print(df1)

df1=df.groupby("Index Name")
#---------------RUSSELL 2000------------------------------------------------------------------------------------------------
Russell_df=df1.get_group("Russell 2000")
#print(Russell_df)

Russell_month=(Russell_df.groupby(pd.Grouper(key='Date', freq='M')).max()).dropna()
Russell_year=Russell_df.groupby(pd.Grouper(key='Date', freq='Y')).max()

#print(Russell_year.loc[Russell_year.Price=="1974.8600"]))
#print(Russell_year.loc["2020-12-31"]["Price"])


Y2021["Russell 2000"]=((Russell_year.loc["2021-12-31"]["Price"]/Russell_year.loc["2020-12-31"]["Price"])-1)*100
#print(Y2021["Russell 2000"])

#-----------------S&P 500-------------------------------------------------------------------------------------------------


sp_df=df1.get_group("S&P 500")
sp_month=(sp_df.groupby(pd.Grouper(key='Date', freq='M')).max()).dropna()
sp_year=sp_df.groupby(pd.Grouper(key='Date', freq='Y')).max()
Y2021["S&P 500"]=((sp_year.loc["2021-12-31"]["Price"]/sp_year.loc["2020-12-31"]["Price"])-1)*100

#--------------Dow Jones 30----------------------------------------------------------------------------------------------------

dow_df=df1.get_group("Dow Jones 30")
dow_month=(dow_df.groupby(pd.Grouper(key='Date', freq='M')).max()).dropna()
dow_year=dow_df.groupby(pd.Grouper(key='Date', freq='Y')).max()
Y2021["Dow Jones 30"]=((dow_year.loc["2021-12-31"]["Price"]/dow_year.loc["2020-12-31"]["Price"])-1)*100

print(Y2021)


