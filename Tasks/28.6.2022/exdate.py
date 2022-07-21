import requests
import pandas as pd
from datetime import datetime,date



url="http://aishvafinancialapi.cmots.com/api/ForthcomigCorporateActions"
data=requests.get(url)


total_data=data.json()['data']

df=pd.DataFrame(total_data)


df["exDate"]=df["exDate"].str.replace('T00:00:00','')
df3=df[df['exDate']<str(date.today())]

df2=df3.groupby("exDate").first()
df4=df2[-5:]

df4=df4.reset_index()

final_data_frame=pd.merge(df, df4, on=['exDate'], how='inner')
co_code_list=list(set(final_data_frame['co_code_x'].to_list()))
print(co_code_list)
second="https://aishvafinancialapi.cmots.com/api/Historical-EOD-Prices/nse/{}/-"

