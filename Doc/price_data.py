import pandas as pd
import quandl
from datetime import datetime

company = pd.read_csv('/home/pallabeedey/Downloads/company-data.csv')
company1=company.rename(columns={'Co_Code':'comp_code','Year End':'date','Co_Name':'comp_name','Sector':'sector','Industry':'industry','Stock Exchange':'stock_code','Equity Paid Up':'equity_paid_up','Net Sales':'net_sales','Debt-Equity Ratio[Latest]':'debt_equity_ratio[Latest]'})
#company 
api_key = "8Htse_SZnFsygUz9xF58"
stck_name = company1['NSE Symbol'].unique()

ln=len(stck_name)
name=[]
for i in range(0,ln):
    name.append(str('NSE/')+str(stck_name[i]))

new_df=company1.groupby('NSE Symbol').agg({'date':"nunique"}) 

b=list(company1['date'])
dte =[]
for i in range(0,9948):
    dte.append(str(b[i])+str('01'))
company1['date']=dte  
company1['date']= pd.to_datetime(company1['date'])
new_data=[]
for i in range(0,4):
    Min=company1[company1['NSE Symbol']== stck_name[i]]['date'].min()
    Max=company1[company1['NSE Symbol']== stck_name[i]]['date'].max()
    data = quandl.get(name[i], authtoken= api_key,start_date=Min, end_date=Max)
    d=pd.DataFrame(data)
    new_data.append(d)
    
    
#new_data  
