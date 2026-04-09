from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, ForeignKey, column
from sqlalchemy import String, Integer, Date
from dateutil import parser
from tkinter import messagebox

Base = declarative_base()

# region Customer class
class Customer(Base):
    __tablename__ = "customer"
    id = Column(Integer, primary_key=True)
    surname = Column(String)
    phone_number = Column(Integer)

    def __repr__(self):
        return f"Customer: {self.id}   Name: {self.surmane}   Phone Number: {self.phone_number}"

    def convert_to_tuple(self):
        return self.id, self.surname, self.phone_number

    def valid(self):
        try:
            value = int(self.phone_number)
        except ValueError:
            return False
        return value >= 0

    @staticmethod
    def convert_from_tuple(tuple_):
        customer = Customer(id=tuple_[0], surname=tuple_[1], phone_number=tuple_[2])
        return customer
# endregion Customer class