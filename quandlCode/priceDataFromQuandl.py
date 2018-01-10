df=pd.DataFrame()

for i in range(0,1752):
    try:
        data = quandl.get(name[i], authtoken= api_key,start_date='2016-01-08', end_date='2018-01-08')
        data=data.reset_index(drop = False)
        data['stock_name']=name[i]
        df = pd.concat([df, data], axis=0)  
    except Exception as e:
        print(str(e))

#df.to_csv("stock_prices.csv") 
