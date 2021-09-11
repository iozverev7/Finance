import uuid

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, VARCHAR, DateTime
from sqlalchemy.sql import func

Base = declarative_base()


class Operation(Base):
    __tablename__ = 'operation'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    date = Column(DateTime(timezone=True), server_default=func.utcnow())
    type = Column(VARCHAR, nullable=True)
    name = Column(VARCHAR, nullable=True)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


class OperationDetails(Base):
    __tablename__ = 'operation_details'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    operation_id = Column(UUID(as_uuid=True), nullable=True)
    position = Column(VARCHAR, nullable=True)
    total_price = Column(Integer, nullable=True)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
