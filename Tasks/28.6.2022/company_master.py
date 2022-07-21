import requests
import pandas as pd
import numpy as np

url="http://aishvafinancialapi.cmots.com/api/CompanyMaster"
data=requests.get(url)


total_data=data.json()['data']
df=pd.DataFrame(total_data)

df2=pd.read_excel(r'C:\Users\nookaraju.c\Downloads\Companymaster_sample.xlsx')

#df['new']=np.where(df['companyname']!=df2['companyname'],'False','True')
#print(df2.columns)

df_comp=df['co_code'].astype(int).to_list()
df2_comp=df2['co_code'].astype(int).to_list()

new_list=list(set(df_comp)-set(df2_comp))



#new_df=df2.copy()

#df2['Flag']=np.select([(df2['Flag']=='New')],[('Listed')],default=df2['Flag'])


df2['Flag']=np.where((df2['Flag']=='New'),'Listed',df2['Flag'])

for i in new_list:
    f=df.loc[df['co_code']==i]
    f['Flag']="New"
    df2=pd.concat([df2, f], ignore_index=True)


#Saishiva bro code
'''
new_comp=df[df['co_code'].isin(new_list)]

new_df=pd.concat([new_comp,df2])


df3=df2.copy()

df3['Flag']=np.select([(df3['Flag']=='New')],[('Listed')],default=df3['Flag'])
'''


