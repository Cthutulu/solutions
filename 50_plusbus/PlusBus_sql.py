from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select, update, delete

from datetime import date

from PlusBus_data import Customer, Journey, Booking,  Base

Database = 'sqlite:///plusbus.db'


def select_all(classparam):
    with Session(engine) as session:
        records = session.scalars(select(classparam))
        result = []
        for record in records:
            result.append(record)
        return result

def get_record(classparam, record_id):
    with Session(engine) as session:
        record = session.scalars(select(classparam).where(classparam.id == record_id)).first()
    return record

def create_record(record):
    with Session(engine) as session:
        record.id = None
        session.add(record)
        session.commit()


# region Customer
'''Customer'''
def update_customer(customer):
    with Session(engine) as session:
        session.execute(update(Customer).where(Customer.id == customer.id).values(surname=customer.surname, phone_number=customer.phone_number))
        session.commit()

def delete_customer(customer):
    with Session(engine) as session:
        session.execute(delete(Customer).where(Customer.id == customer.id))
        session.commit()


# endregion Customer

# region Journey
def update_journey(journey):
    with Session(engine) as session:
        session.execute(update(Journey).where(Journey.route == journey.route).values(date=journey.date, capacity=journey.capacity))
        session.commit()

def delete_journey(journey):
    with Session(engine) as session:
        session.execute(delete(Journey).where(Journey.route == journey.route))
        session.commit()
# endregion Journey

# region booking
def update_booking(booking):
    with Session(engine) as session:
        session.execute(update(Booking).where(Booking.id == booking.id).values(journey_id=booking.journey_id, journey_route=booking.journey_route, customer_id=booking.customer_id, booked_seats=booking.booked_seats))
        session.commit()

def delete_booking(booking):
    with Session(engine) as session:
        session.execute(delete(Booking).where(Booking.id == booking.id))
        session.commit()
# endregion booking




if __name__ == "__main__":
    engine = create_engine(Database, echo=False, future=True)
    Base.metadata.create_all(engine)
else:
    engine = create_engine(Database, echo=False, future=True)
    Base.metadata.create_all(engine)
