from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modtab import Exchange
import pandas as pd


engine = create_engine('sqlite:///orm2.db')

Session = sessionmaker(bind=engine)
session = Session()


exch = pd.read_csv('/home/pallabeedey/Indian_fins/data/exchn.csv')
l1=len(exch)

for i in range(0,l1):
    code= exch['exch_code'][i]
    name= exch['exch_name'][i]
    session.add(Exchange(name, code))
    
session.commit()    
    

