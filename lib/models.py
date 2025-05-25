from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Company(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    founding_year = Column(Integer)
    freebies = relationship("Freebie", back_populates="company")

class Dev(Base):
    __tablename__ = "devs"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    freebies = relationship("Freebie", back_populates="dev")

class Freebie(Base):
    __tablename__ = "freebies"
    id = Column(Integer, primary_key=True)
    item_name = Column(String)
    value = Column(Integer)
    dev_id = Column(Integer, ForeignKey("devs.id"))
    company_id = Column(Integer, ForeignKey("companies.id"))
    dev = relationship("Dev", back_populates="freebies")
    company = relationship("Company", back_populates="freebies")
