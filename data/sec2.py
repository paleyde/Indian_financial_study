import pandas as pd
company = pd.read_csv('/home/pallabeedey/Downloads/company-data.csv')
company1=company.rename(columns={'Co_Code':'comp_code','Year End':'date','Co_Name':'comp_name','Sector':'sector','Industry':'industry','Stock Exchange':'stock_code','Equity Paid Up':'equity_paid_up','Net Sales':'net_sales','Debt-Equity Ratio[Latest]':'debt_equity_ratio[Latest]'})
col3=company1['sector'].unique()
l1=len(col3)
s1=[]
for i in range(0,l1):
    s1.append(str('S')+str(i))
b=pd.DataFrame({'sector_code':s1,'sector_name':col3})
b.to_csv("sec2.csv")
