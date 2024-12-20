from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from .base import Base

class Platform(Base):
    __tablename__ = 'platforms'

    platform_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    coin_address = Column(String(255))
    
    coins = relationship("Coin", back_populates="platform")