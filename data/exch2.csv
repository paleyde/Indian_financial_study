import pandas as pd
company = pd.read_csv('/home/pallabeedey/Downloads/company-data.csv')
company1=company.rename(columns={'Co_Code':'comp_code','Year End':'date','Co_Name':'comp_name','Sector':'sector','Industry':'industry','Stock Exchange':'stock_code','Equity Paid Up':'equity_paid_up','Net Sales':'net_sales','Debt-Equity Ratio[Latest]':'debt_equity_ratio[Latest]'})
col1=company1['stock_code'].unique()
l=len(col1)
s=['National Stock Exchange','National Stock Exchange-small and medium enterprise']
a=pd.DataFrame({'exch_code':col1,'exch_name':s})
a.to_csv("exchn.csv")
