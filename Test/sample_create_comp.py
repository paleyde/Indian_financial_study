import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
import pandas as pd

engine = sqlalchemy.create_engine('sqlite:///smpl.db')
Base = declarative_base()

nw=pd.read_csv('/home/pallabeedey/company_industry_sector_data.csv')
nw1=pd.read_csv('/home/pallabeedey/sector_company_industry_by_nos.csv')

class Company(Base):
    __tablename__ = 'company'
    id = Column(Integer, primary_key=True)
    sector_id = Column(Integer, ForeignKey('sector.id'), primary_key=True)
    industry_id = Column(Integer, ForeignKey('industry.id'), primary_key=True)
    name = Column(String(80), nullable=False)

class Industry(Base):
    __tablename__ = 'industry'
    id = Column(Integer, primary_key=True)
    
    name = Column(String(80), nullable=False)
    s = relationship('Company', backref='industry',
                         primaryjoin=id == Company.industry_id)    
                         
    def __init__(self, name):
        
        self.name = name

    def __repr__(self):
        return "Industry(ind_id={self.ind_id}, name={self.name})".format(self=self)
        
class Sector(Base):
    __tablename__ = 'sector'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    s = relationship('Company', backref='sector',
                         primaryjoin=id == Company.sector_id)
       
                         
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Stock {}>'.format(self.name)
        
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

c_id = 0
for i in range(0,72):
    sec = nw1["sector_name"][i]
    Se = Sector(name= sec)
    l = nw1["comp_nos"][i]
    ind1=[]
    for j in range(0,l):
       
       ind = nw["industry_name"][c_id]
       if ind not in ind1:
           ind1.append(ind)
           In = Industry(name= ind)
           comp= nw["company"][c_id]
           COMP=Company(id= (c_id+1), sector_id= Se.id, industry_id= In.id, name= comp)
           Se.s.append(COMP)
           In.s.append(COMP)
       else:
      
           comp= nw["company"][c_id]
           COMP=Company(id= (c_id+1), sector_id= Se.id, industry_id= In.id, name= comp)
           Se.s.append(COMP)
           In.s.append(COMP)
               
       session.add(In)
       c_id = c_id+1
    session.add(Se)       
    
session.commit()
