from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from lib.db.base import Base

# Association table
event_attendees = Table(
    'event_attendees', Base.metadata,
    Column('event_id', Integer, ForeignKey('events.id')),
    Column('attendee_id', Integer, ForeignKey('attendees.id'))
)

class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    date = Column(String(50), nullable=False)
    location = Column(String(50))

    attendees = relationship(
        'Attendee', secondary=event_attendees, back_populates='events'
    )

    def __repr__(self):
        return f"<Event(name='{self.name}', date='{self.date}')>"

class Attendee(Base):
    __tablename__ = 'attendees'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, nullable=False)

    events = relationship(
        'Event', secondary=event_attendees, back_populates='attendees'
    )

    def __repr__(self):
        return f"<Attendee(name='{self.name}', email='{self.email}')>"