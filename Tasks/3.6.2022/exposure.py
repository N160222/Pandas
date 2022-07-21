import pandas as pd
df1=pd.read_excel("C:\\Users\\nookaraju.c\\Downloads\\Task3.xlsx","Prices_Input")
df2=pd.read_excel("C:\\Users\\nookaraju.c\\Downloads\\Task3.xlsx","Quantity_Input")

newdf=df1[["Company","Date","Price"]].merge(df2[["Company","Quantity"]],on="Company",how="left")
newdf=newdf.sort_values(by = 'Date')
newdf["Exposure"]=newdf["Price"]*newdf["Quantity"]
Total_Exposure= newdf.groupby("Date",as_index =False)["Exposure"].sum()
Total_Exposure.columns=["Date","Total_Exposure"]
final_df=newdf[["Company","Date","Price","Quantity","Exposure"]].merge(Total_Exposure[["Date","Total_Exposure"]],on="Date",how="left")


final_df.to_excel("C://Users//nookaraju.c//Desktop//Tasks//3.6.2022//Output.xlsx")