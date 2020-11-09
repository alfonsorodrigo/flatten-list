from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Flatten(Base):
    __tablename__ = "flatten"
    id = Column(Integer, primary_key=True)
    items = Column(String)
    result = Column(String)

    def __repr__(self):
        return "items : {}, result: {}".format(self.items, self.result)
