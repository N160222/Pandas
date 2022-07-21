import pandas as pd


df=pd.read_excel(r'C:\Users\nookaraju.c\Downloads\MA_Calc.xlsx')
df=df.sort_values(by=["Company_Code","Date"],ascending = True)
imp_df=df.copy()
final_df=df.copy()
df2=df.groupby(by=["Company_Code"],as_index=False,sort=True)['Adj Price Close'].rolling(window=9).mean()


df2=pd.DataFrame(df2)
df2=df2["Adj Price Close"]
final_df=pd.merge(final_df,df2, left_index=True, right_index=True)




df=imp_df.copy()

df2=df.groupby(by=["Company_Code"],as_index=False,sort=True)['Adj Price Close'].rolling(window=20).mean()


df2=pd.DataFrame(df2)
df2=df2["Adj Price Close"]
final_df=pd.merge(final_df,df2, left_index=True, right_index=True)



df=imp_df.copy()

df2=df.groupby(by=["Company_Code"],as_index=False,sort=True)['Adj Price Close'].rolling(window=50).mean()


df2=pd.DataFrame(df2)
df2=df2["Adj Price Close"]
final_df=pd.merge(final_df,df2, left_index=True, right_index=True)





#print(df2.columns)

#df3=df.merge(df2,how="inner", on=['Company_Code'])




#[["Date","Company_Code","Add Price Close"]]

#df2=df.groupby(by=["Company_Code"],sort=True)
#df2=df2.get_group(476)['Adj Price Close'].rolling(window=9).mean()
'''
MA=df2["Adj Price Close"]
MA.columns="MA9"
df=df.join(MA)'''