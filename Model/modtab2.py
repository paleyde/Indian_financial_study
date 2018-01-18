from sqlalchemy import Column, Integer, Float, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey, ForeignKeyConstraint
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

class Industry(Base):
    """class Industry"""  
    __tablename__ = 'industry'
    id = Column(Integer, primary_key=True)
    code = Column(String(80), nullable=False, unique=True, index=True)
    name = Column(String(80), nullable=False, unique=True, index=True)

    
    def __init__(self,code,name):
        self.code = code
        self.name = name
        
    def __repr__(self):    
        return "<Industry(code='%s', name='%s')>" % ( self.code,self.name)    
        
class Sector(Base):
    """class Sector"""  
    __tablename__ = 'sector'
    id = Column(Integer, primary_key=True)
    code = Column(String(80), nullable=False, unique=True, index=True)
    name = Column(String(80), nullable=False, unique=True, index=True)
    
    
    def __init__(self,code,name):
        self.code = code
        self.name = name  
    
    def __repr__(self):    
        return "<Sector(code='%s', name='%s')>" % ( self.code,self.name)    

class Exchange(Base):
    """class exchange"""
    __tablename__ = 'exchange'
    id = Column(Integer, primary_key=True)
    code = Column(String(40), nullable=False, unique=True, index=True)
    name = Column(String(40), nullable=False, unique=True, index=True)
     

    def __init__(self, code, name):
        self.code = code
        self.name = name
    
    def __repr__(self):    
        return "<Exchange(code='%s', name='%s')>" % ( self.code,self.name)

class Company(Base):
    """class Company"""
    __tablename__ = 'company'
    id = Column(Integer, primary_key=True)
    code = Column(String(40), nullable=False, unique=True, index=True)
    name = Column(String(40), nullable=False, unique=True, index=True)
    industry_name = Column(String(40), ForeignKey('industry.name'))
    sector_name = Column(String(40), ForeignKey('sector.name'))
    industry = relationship("Industry", back_populates = "Companies")
    sector = relationship("Sector", back_populates = "Companies")
    
    
    def __init__(self,code,name,industry_name,sector_name):
        self.code = code
        self.name = name
        self.industry_name = industry_name
        self.sector_name = sector_name
    
    def __repr__(self):    
        return "<Company(code='%s',name='%s',industry_name='%s',"\
               "sector_name='%s')>" %          ( self.code,self.name,self.industry_name,self.sector_name)
        
