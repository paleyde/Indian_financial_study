from sqlalchemy import Column, Integer, Float, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey, ForeignKeyConstraint
from sqlalchemy.orm import relationship, backref

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import pandas as pd

Base = declarative_base()

class Sector(Base):
    """class Sector"""  
    __tablename__ = 'sector'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False, unique=True, index=True)
    companies = relationship("Company", back_populates = "sector")
    
class Company(Base):
    """class Company"""
    __tablename__ = 'company'
    id = Column(Integer, primary_key=True)
    sector_name = Column(String(40), ForeignKey('sector.id'))
    sector = relationship("Sector", back_populates = "companies")
 
 

engine = create_engine('sqlite:///sector_comp.db')
session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine) 
s = session()    

sect = pd.read_csv('/home/pallabeedey/Indian_fins/data/sec2.csv')
l1 = len(sect)
cs = pd.read_csv('/home/pallabeedey/Indian_fins/data/comp_sect_ind.csv')
l=len(cs)

for i in range(0,l):
    sec_name = cs['sector'][i]
    sect_name = Sector(name= sec_name)
    c = cs['comp_name'][i]
    print c
    for j in range(0,c):
        comp_name = cs['comp_name'][i]
        comp_name = Company(sector = sect_name)
        s.add(comp_name)
        
s.commit()        
        


