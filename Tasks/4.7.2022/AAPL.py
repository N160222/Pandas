import requests
import pandas as pd


url="https://eodhistoricaldata.com/api/fundamentals/AAPL.US?api_token=612f4f7f3906a3.86934021&fmt=json"
data=requests.get(url)


second_data=data.json()["General"]
first_data=data.json()["Highlights"]
first_data_tech=data.json()["Technicals"]
first_data_anr=data.json()["AnalystRatings"]
first_data_tr=data.json()["Valuation"]
first_data_ss=data.json()["SharesStats"]
first_data_sd=data.json()["SplitsDividends"]

first_data.update(first_data_tech)
first_data.update(first_data_anr)
first_data.update(first_data_tr)
first_data.update(first_data_ss)
first_data.update(first_data_sd)
first_data=pd.DataFrame(first_data)
first_data=first_data.sort_index(axis=1).reset_index().loc[0]
first_data=pd.DataFrame(first_data).T
first_data.drop(['index'], axis = 1,inplace=True)
first_data.insert(0,"Ticker",second_data['Code'])

df=pd.DataFrame(second_data)
df=df.select_dtypes(include=['object']).reset_index()
Master_data=df.loc[0, ~df.columns.isin(['Officers', 'AddressData','Description', "Listings"])]
Master_data=pd.DataFrame(Master_data).T
Master_data.drop(['index'], axis = 1,inplace=True)
Master_data=Master_data.sort_index(axis=1)
Master_data.insert(0,"Ticker",second_data['Code'])


officers=second_data["Officers"]
officers_df=pd.DataFrame(officers).T
officers_df["Ticker"]=second_data['Code']

descript={
    "Ticker":[second_data['Code']],
    "Description":[second_data["Description"]]
    }
descript=pd.DataFrame(descript)

with pd.ExcelWriter('C:\\Users\\nookaraju.c\\Desktop\\Tasks\\4.7.2022\\Final_Output.xlsx') as writer:
    first_data.to_excel(writer, sheet_name="Master Data",index=False)
    Master_data.to_excel(writer, sheet_name="Description",index=False)
    officers_df.to_excel(writer, sheet_name="Officers",index=False)
    descript.to_excel(writer, sheet_name="TTM Data",index=False)
'''
first_data.to_excel("C:\\Users\\nookaraju.c\\Desktop\\Tasks\\4.7.2022\\Final_Output.xlsx",sheet_name="Master Data",index=False)
Master_data.to_excel("C:\\Users\\nookaraju.c\\Desktop\\Tasks\\4.7.2022\\Final_Output.xlsx",sheet_name="Description",index=False)
officers_df.to_excel("C:\\Users\\nookaraju.c\\Desktop\\Tasks\\4.7.2022\\Final_Output.xlsx",sheet_name="Officers",index=False)
descript.to_excel("C:\\Users\\nookaraju.c\\Desktop\\Tasks\\4.7.2022\\Final_Output.xlsx",sheet_name="TTM Data",index=False)
'''

