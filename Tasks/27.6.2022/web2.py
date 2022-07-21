import requests
import pandas as pd


url="https://eodhistoricaldata.com/api/fundamentals/AAPL.US?api_token=612f4f7f3906a3.86934021&fmt=json"
data=requests.get(url)

total_data=data.json()['Financials']
#Balance_Sheet-------quarterly
Balance_Sheet_qua=total_data['Balance_Sheet']['quarterly']
Balance_Sheet_qua_final=(pd.DataFrame(Balance_Sheet_qua)).T

#Balance_Sheet-------Yearly

Balance_Sheet_yearly=total_data['Balance_Sheet']['yearly']
Balance_Sheet_yearly_final=(pd.DataFrame(Balance_Sheet_yearly)).T

#Cash_Flow quarterly

Cash_Flow_qua=total_data['Cash_Flow']['quarterly']
Cash_Flow_qua_Final=(pd.DataFrame(Cash_Flow_qua)).T

#Cash_Flow yearly
Cash_Flow_yearly=total_data['Cash_Flow']['yearly']
Cash_Flow_yearly_Final=(pd.DataFrame(Cash_Flow_yearly)).T

#Income_Statement quarterly

Income_Statement_qua=total_data['Income_Statement']['quarterly']
Income_Statement_qua_Final=(pd.DataFrame(Income_Statement_qua)).T

#Income_Statement yearly

Income_Statement_yearly=total_data['Income_Statement']['yearly']
Income_Statement_yearly_Final=(pd.DataFrame(Income_Statement_yearly)).T



