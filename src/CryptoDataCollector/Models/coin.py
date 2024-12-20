from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Coin(Base):
    __tablename__ = 'coins'

    coin_id = Column(String(100), primary_key=True)
    symbol = Column(String(20), nullable=False)
    name = Column(String(100), nullable=False)
    market_cap = Column(Float)
    current_price = Column(Float)
    total_volume = Column(Float)
    platform_id = Column(Integer, ForeignKey('platforms.platform_id'))
    
    platform = relationship("Platform", back_populates="coins")