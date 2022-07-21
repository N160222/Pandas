import requests
import pandas as pd


def company_master():
    url="http://aishvafinancialapi.cmots.com/api/CompanyMaster"
    data=requests.get(url)
    
    total_data=data.json()['data']
    df=pd.DataFrame(total_data)
    
#https://eodhistoricaldata.com/api/eod/MCD.US?api_token=OeAFFmMliFG5orCUuwAKQ8l4WWFQ67YX&period=d&fmt=json&order=d&from=2017-01-05&to=2017-02-10&filter=last_close
#612f4f7f3906a3.86934021

def histrorical_price():
    url="https://aishvafinancialapi.cmots.com/api/Historical-EOD-Prices/nse/6/-"
    data=requests.get(url)
    total_data=data.json()['data']
    df1=pd.DataFrame(total_data)
    date_6=df1
    
    url="https://aishvafinancialapi.cmots.com/api/Historical-EOD-Prices/nse/476/-"
    data=requests.get(url)
    total_data=data.json()['data']
    df1=pd.DataFrame(total_data)
    date_476=df1
    
    url="https://aishvafinancialapi.cmots.com/api/Historical-EOD-Prices/nse/5400/-"
    data=requests.get(url)
    total_data=data.json()['data']
    df1=pd.DataFrame(total_data)
    date_5400=df1
    return date_6,date_476,date_5400
date_6,date_476,date_5400=histrorical_price()

'''comany_list=[6,476,5400]
for i in comany_list:
    url="https://aishvafinancialapi.cmots.com/api/Historical-EOD-Prices/nse/{}/-".format(i)
    data=requests.get(url)
    total_data=data.json()['data']
    df1=pd.DataFrame(total_data)
    
    date_num="date_"+str(i)
    print(date_num)
    date_num=df1
    
    '''