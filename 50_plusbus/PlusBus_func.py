from sqlalchemy.orm import Session
from sqlalchemy import select

import PlusBus_data as pbd
import PlusBus_sql as pbsql

def booked_seats(journey):
    with Session(pbsql.engine) as session:
        records = session.scalars(select(pbd.Booking).where(pbd.Booking.journey_id == journey.id))
        seats = 0
        for record in records:
            seats += int(record.booked_seats)
    return seats

def capacity_available(journey, new_booking):
    booked = booked_seats(journey)
    return journey.capacity >= booked + int(new_booking.booked_seats)
