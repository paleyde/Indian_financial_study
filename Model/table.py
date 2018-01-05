from sqlalchemy import Column, Integer, Float, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey, ForeignKeyConstraint
from sqlalchemy.orm import relationship, backref

Base = declarative_base()



class Exchange(Base):
    """class exchange"""
    __tablename__ = 'exchange'
    code = Column(String(40), primary_key=True)
    name = Column(String(40), nullable=False, unique=True, index=True)
     

    def __init__(self, code, name):
        self.code = code
        self.name = name
    
    def __repr__(self):    
        return "<Exchange(code='%s', name='%s')>" % ( self.code,self.name)
                                 
        
class Industry(Base):
    """class Industry"""  
    __tablename__ = 'industry'
    code = Column(String(80), primary_key=True)
    name = Column(String(80), nullable=False, unique=True, index=True)
    
    def __init__(self,code,name):
        self.code = code
        self.name = name
        
    def __repr__(self):    
        return "<Industry(code='%s', name='%s')>" % ( self.code,self.name)    
        
class Sector(Base):
    """class Sector"""  
    __tablename__ = 'sector'
    code = Column(String(80), primary_key=True)
    name = Column(String(80), nullable=False, unique=True, index=True)
    
    def __init__(self,code,name):
        self.code = code
        self.name = name  
    
    def __repr__(self):    
        return "<Sector(code='%s', name='%s')>" % ( self.code,self.name)    

class Company(Base):
    """class Company"""
    __tablename__ = 'company'
    code = Column(String(40), primary_key=True)
    name = Column(String(40), nullable=False, unique=True, index=True)
    
    def __init__(self,code,name):
        self.code = code
        self.name = name
    
    def __repr__(self):    
        return "<Company(code='%s', name='%s')>" % ( self.code,self.name)
        
class CompanyFinancial(Base):
    """class CompanyFinancial"""
    __tablename__ = 'company_financial'
    date = Column(DateTime, primary_key = True)
    code = Column(Integer, ForeignKey('company.code'), primary_key = True)
    comp_code = Column(String(40), ForeignKey('company.code'))
    company = relationship(Company,backref=backref('financial',uselist=True,
                         cascade='delete,all'))                                 
                         
    equity_paid_up = Column(Float, nullable=False, unique=True, index=True)
    net_sales =  Column(Float, nullable=False, unique=True, index=True)
    PA_tax = Column(Float, nullable=False, unique=True, index=True)
    PBIDT = Column(Float, nullable=False, unique=True, index=True)
    debt_equity_ratio = Column(Float, nullable=False, unique=True, index=True)
    PBITM_perc = Column(Float, nullable=False, unique=True, index=True)
   
    def __init__(self,date):
        self.date = date
        self.equity_paid_up = equity_paid_up
        self.net_sales = net_sales
        self.PA_tax = PA_tax
        self.PBIDT = PBIDT
        self.debt_equity_ratio = debt_equity_ratio
        self.PBITM_perc = PBITM_perc
       
    def __repr__(self):    
        return "<CompanyFinancial(date ='%s', equity_paid_up='%f,"\
               "net_sales= %f, PA_tax= %f, PBIDT= %f,"\
                "debt_equity_ratio= %f, PBITM_perc= %f  ')>" %           ( self.date,self.equity_paid_up,self.net_sales,self.PA_tax,
                self.PBIDT,self.debt_equity_ratio,self.PBITM_perc)
       
class Stock(Base):
    """class Stock"""
    __tablename__ = 'stock'
    comp_code = Column(String(40), ForeignKey('company.code'), primary_key = True)
    exch_code = Column(String(40), ForeignKey('exchange.code'), primary_key = True)
    symbol = Column(String(40), nullable=False, index=True)
    company = relationship(Company,backref=backref('stock',uselist=True,
                         cascade='delete,all'))   
    exchange = relationship(Exchange,backref=backref('stock',uselist=True,
                         cascade='delete,all'))
   
    def __init__(self,symbol):
        self.symbol = symbol
                        
    def __repr__(self):    
        return "<Stock(code='%s', name='%s, symbol= %s')>" % ( self.code,self.name,self.symbol)
        
                         
