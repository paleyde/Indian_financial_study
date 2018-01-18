import pandas as pd
company = pd.read_csv('/home/pallabeedey/Downloads/company-data.csv')
company1=company.rename(columns={'Co_Code':'comp_code','Year End':'date','Co_Name':'comp_name','Sector':'sector','Industry':'industry','Stock Exchange':'stock_code','Equity Paid Up':'equity_paid_up','Net Sales':'net_sales','Debt-Equity Ratio[Latest]':'debt_equity_ratio[Latest]'})
col4=company1['industry'].unique()
l2=len(col4)
s2=[]
for i in range(0,l2):
    s2.append(str('I')+str(i))
c=pd.DataFrame({'industry_code':s2,'industry_name':col4})
c.to_csv("ind2.csv")
