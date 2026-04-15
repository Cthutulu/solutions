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
        return f"Customer: {self.id}   Name: {self.surname}   Phone Number: {self.phone_number}"

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

# region Journey class
class Journey(Base):
    __tablename__ = "journey"
    id = Column(Integer, primary_key=True)
    route = Column(String)
    date = Column(Date)
    capacity = Column(Integer)

    def __repr__(self):
        return f"Journey Route: {self.route}   Date: {self.date}   Capacity: {self.capacity}"

    def convert_to_tuple(self):
        return self.route, self.date, self.capacity

    def valid(self):
        try:
            value = int(self.capacity)
        except ValueError:
            return False
        return value >= 0

    @staticmethod
    def convert_from_tuple(tuple_):
        capacity = int(tuple_[2])
        if capacity <= 0:
            messagebox.showwarning("", "No space left on journey!")
        else:
            date = parser.parse(tuple_[1])
            journey = Journey(route=tuple_[0], date=date, capacity=capacity)
            return journey
# endregion Journey class

# region booking class
class Booking(Base):
    __tablename__ = "booking"
    journey_route = Column(String, ForeignKey("journey.route"), nullable=False, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customer.id"), nullable=False)
    booked_seats = Column(Integer)

    def __repr__(self):
        return f""

    def convert_to_tuple(self):
        return self.journey_route, self.customer_id, self.booked_seats

    def valid(self):
        try:
            value = int(self.customer_id)
        except ValueError:
            return False
        return value >= 0


# endregion booking class