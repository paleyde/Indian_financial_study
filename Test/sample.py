import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
import pandas as pd


engine = sqlalchemy.create_engine('sqlite:///sample1.db')
Base = declarative_base()


class Company(Base):
    __tablename__ = 'company'
    id = Column(Integer, primary_key=True)
    sector_id = Column(Integer, ForeignKey('sector.id'), primary_key=True)
    industry_id = Column(Integer, ForeignKey('industry.id'), primary_key=True)
    name = Column(String(80), nullable=False)

class Industry(Base):
    __tablename__ = 'industry'
    id = Column(Integer, primary_key=True)
    ind_id = Column(Integer, nullable=False)
    name = Column(String(80), nullable=False)
    s = relationship('Company', backref='industry',
                         primaryjoin=id == Company.industry_id)    
                         
    def __init__(self, ind_id ,name):
        self.ind_id = ind_id
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
   
s1 = Sector(name="bank")
s2 = Sector(name="cement")
s3 = Sector(name="chem")

i1 = Industry(ind_id=1,name="private")
i2 = Industry(ind_id=2,name="public")
i3 = Industry(ind_id=3,name="natural")
i4 = Industry(ind_id=4,name="al")
i5 = Industry(ind_id=5,name="al_sht")

op1 = Company(id=1, sector_id=s1.id, industry_id=i1.id, name="vijaya")
s1.s.append(op1)
i1.s.append(op1)

op2 = Company(id=2, sector_id=s1.id, industry_id=i2.id, name="sbi")
s1.s.append(op2)
i2.s.append(op2)

op3 = Company(id=3, sector_id=s2.id, industry_id=i3.id, name="CO2")
s2.s.append(op3)
i3.s.append(op3)

op4 = Company(id=4, sector_id=s3.id, industry_id=i4.id, name="hind")
s3.s.append(op4)
i4.s.append(op4)

op5 = Company(id=5, sector_id=s3.id, industry_id=i4.id, name="man")
s3.s.append(op5)
i4.s.append(op5)

op6 = Company(id=6, sector_id=s3.id, industry_id=i5.id, name="par")
s3.s.append(op6)
i5.s.append(op6)

op7 = Company(id=7, sector_id=s3.id, industry_id=i5.id, name="glob")
s3.s.append(op7)
i5.s.append(op7)



session.add_all([s1, s2,s3,i1,i2,i3,i4,i5])
session.commit()
