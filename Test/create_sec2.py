from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sect_comp import Sector
import pandas as pd

engine = create_engine('sqlite:///sector_comp.db')

Session = sessionmaker(bind=engine)
session = Session()


s = pd.read_csv('/home/pallabeedey/Indian_fins/data/sec2.csv')
l1=len(s)

for i in range(0,l1):
    code= s['sector_code'][i]
    name= s['sector_name'][i]
    session.add(Sector(name, code))
    
session.commit()
