import pandas as pd
company = pd.read_csv('/home/pallabeedey/Downloads/company-data.csv')
company1=company.rename(columns={'Co_Code':'comp_code','Year End':'date','Co_Name':'comp_name','Sector':'sector','Industry':'industry','Stock Exchange':'stock_code','Equity Paid Up':'equity_paid_up','Net Sales':'net_sales','Debt-Equity Ratio[Latest]':'debt_equity_ratio[Latest]'})
#company   
comp=company1.groupby('comp_code').agg({'comp_name': "first"})
#comp.to_csv("company.csv")
#exchange 
col1=company1['stock_code'].unique()
l=len(col1)
s=['National Stock Exchange','National Stock Exchange-small and medium enterprise']
a=pd.DataFrame({'exch_code':col1,'exch_name':s})
exch=a.set_index('exch_code')
#exch.to_csv("exchange.csv")
#company_financials    
data=company1.rename(columns={'Year End':'date'})
comp_finc = company1[['comp_code', 'date', 'equity_paid_up', 'net_sales', 'PAT', 'PBIDT', 'debt_equity_ratio[Latest]', 'PBIDTM (%)[Latest]' ]].set_index(['comp_code', 'date'])
#comp_finc.to_csv("company_financial.csv")
#sector
col3=company1['sector'].unique()
l1=len(col3)
s1=[]
for i in range(0,l1):
    s1.append(str('S')+str(i))
b=pd.DataFrame({'sector_code':s1,'sector_name':col3})
sect=b.set_index('sector_code')
#sect.to_csv("sector.csv")
#industry
col4=company1['industry'].unique()
l2=len(col4)
s2=[]
for i in range(0,l2):
    s2.append(str('I')+str(i))
c=pd.DataFrame({'industry_code':s2,'industry_name':col4})
ind=c.set_index('industry_code')
#ind.to_csv("industry.csv")
stock=company1.groupby('comp_code').agg({'NSE Symbol': "first",'stock_code':"first"})
stck=stock.rename(columns={'NSE Symbol':'stock_symbol','stock_code':'exch_code'})
stck.to_csv("stock.csv")
