import pandas as pd


df=pd.read_excel(r'C:\Users\nookaraju.c\Downloads\EMA_Calc.xlsx',sheet_name="Input")
df=df.sort_values(by=["Company_Code","Date"],ascending = True).reset_index()

final_df=df.copy()
#df2=df.groupby(by=["Company_Code"],as_index=False,sort=True)['Adj Price Close'].rolling(window=9).mean()
df2=df.groupby(by=["Company_Code"],as_index=False,sort=True)['Adj Price Close'].ewm(span=9, adjust=False).mean()

df2=pd.DataFrame(df2).reset_index()
df2=df2["Adj Price Close"]
df2.columns=["MA9"]
final_df=pd.merge(df,df2, left_index=True, right_index=True)
final_df=final_df[['Company_Code', 'Date', 'Adj Price Close_x','Adj Price Close_y']]















'''
df2=df.groupby(by=["Company_Code"],as_index=False)['Adj Price Close_x'].ewm(span=9, adjust=False).mean()

df2=pd.DataFrame(df2)


#df2=df2["Adj Price Close_x"]
#final_df=final_df.join(df2)
#final_df["EMA9"]=df2["Adj Price Close_x"]
df2=df2["Adj Price Close_x"]

final_df=pd.merge(final_df,df2,left_index=True,right_index=True)
'''
#print(final_df)

'''
df3=df.groupby(by=["Company_Code"],as_index=False)

df4=df3.get_group(476)
df4["EMA"]=df4['Adj Price Close_x'].ewm(span=9).mean()

['Company_Code', 'Date', 'Adj Price Close_x', 'Adj Price Close_y']

df2.columns=["MA9"]

df2=df2.ewm(span=1, adjust=False).mean()

final_df=pd.merge(final_df,df2, left_index=True, right_index=True)

'''


#df['4dayEWM'] = df['sales'].ewm(span=4, adjust=False).mean()