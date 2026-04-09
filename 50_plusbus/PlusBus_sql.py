from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select, update, delete

from datetime import date

from PlusBus_data import Customer, Base

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


# endregion Customer








if __name__ == "__main__":  # Executed when invoked directly
    engine = create_engine(Database, echo=False, future=True)
    Base.metadata.create_all(engine)
#     select_all(Transport)
#     print(get_record(Customer, 2))
#     print(get_record(Aircraft, 3))
else:  # Executed when imported
    engine = create_engine(Database, echo=False, future=True)
    Base.metadata.create_all(engine)
