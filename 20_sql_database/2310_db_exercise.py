"""
Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

--------

Anvend det, du har lært i dette kapitel om databaser, på en denne opgave.

Trin 1:
Opret en ny SQLite database "2311_my_second_sql_database.db" i din solutions mappe.
Denne database skal indeholde 2 tabeller.
Den første tabel skal hedde "customers" og repræsenteres i Python-koden af en klasse kaldet "Customer".
Tabellen bruger sin første attribut "id" som primærnøgle.
De andre attributter i tabellen hedder "name", "address" og "age".
Definer selv fornuftige datatyper for attributterne.

Trin 2:
Den anden tabel skal hedde "products" og repræsenteres i Python-koden af en klasse kaldet "Product".
Denne tabel bruger også sin første attribut "id" som primærnøgle.
De andre attributter i tabellen hedder "product_number", "price" og "brand".

Trin 3:
Skriv en funktion create_test_data(), der opretter testdata for begge tabeller.

Trin 4:
Skriv en metode __repr__() for begge dataklasser, så du kan vise poster til testformål med print().

Til læsning fra databasen kan du genbruge de to funktioner select_all() og get_record() fra 2240_db_class_methods.py.

Trin 5:
Skriv hovedprogrammet: Det skriver testdata til databasen, læser dataene fra databasen med select_all() og/eller get_record() og udskriver posterne til konsollen med print().

--------

Når dit program er færdigt, skal du skubbe det til dit github-repository.
"""

from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy import create_engine, select

Database = 'sqlite:///2311_my_second_sql_database.db'
Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f"Customer(ID:{self.id}    Name:{self.name}    Address:{self.address}    Age:{self.age})"

    def convert_to_tuple(self):
        return self.id, self.name, self. address, self.age

    def valid(self):
        try:
            value = int(self.age)
        except ValueError:
            return False
        return value >= 0


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    product_number = Column(Integer)
    price = Column(Float)
    brand = Column(String)

    def __repr__(self):
        return f"Product(ID:{self.id}    Product Number:{self.product_number}    Price:{self.price}    Brand:{self.brand})"

    def convert_to_tuple(self):
        return self.id, self.product_number, self.price, self.brand

    def valid(self):
        try:
            value = int(self.price)
        except ValueError:
            return False
        return value >= 0

def create_test_data():
    with Session(engine) as session:
        new_item = []
        new_item.append(Customer(name="james", address="4276 Huel Port", age=32))
        new_item.append(Customer(name="Elizabeth", address="Nielslaan 924", age=53))
        new_item.append(Customer(name="Richard", address="Ottostr. 688", age=62))
        new_item.append(Customer(name="Jessica", address="9458 Earlene Tunnel", age=43))
        new_item.append(Customer(name="Christopher", address="Palackého 788", age=25))
        new_item.append(Customer(name="Daniel", address="Vestre Bjørkeskrenten 90", age=35))
        new_item.append(Customer(name="Emily", address="Strada Zefiro 7", age=46))
        new_item.append(Customer(name="Steven", address="Michielsstraat 578b", age=20))
        new_item.append(Customer(name="Amanda", address="Idrottsgränden 9", age=42))
        new_item.append(Customer(name="Timothy", address="10 Impasse Saint-Jacques", age=38))
        new_item.append(Customer(name="Laura", address="060 Crystal Turnpike", age=83))

        new_item.append(Product(product_number=31, price=44.95, brand="Ikea"))
        new_item.append(Product(product_number=27, price=300.00, brand="Apple"))
        new_item.append(Product(product_number=61, price=34.95, brand="Logitech"))
        new_item.append(Product(product_number=49, price=5.95, brand="USPC"))
        new_item.append(Product(product_number=63, price=20.00, brand="Knoll"))
        new_item.append(Product(product_number=17, price=44.95, brand="Lego"))
        new_item.append(Product(product_number=3, price=2.95, brand="Denso"))
        new_item.append(Product(product_number=74, price=4.00, brand="Coca Cola"))
        new_item.append(Product(product_number=23, price=52.45, brand="Nemco"))
        new_item.append(Product(product_number=91, price=52.75, brand="Indigo"))

        session.add_all(new_item)
        session.commit()


engine = create_engine(Database, echo=False, future=True)
Base.metadata.create_all(engine)

create_test_data()

def select_all(classparam):
    with Session(engine) as session:
        records = session.scalars(select(classparam))
        result = []
        for record in records:
            result.append(record)
        print(records)
    return result


def get_record(classparam, record_id):
    with Session(engine) as session:
        record = session.scalars(select(classparam).where(classparam.id == record_id)).first()
    return record

print(get_record(Customer, 8))
print(get_record(Product, 1))
print(select_all(Customer))

