from lib.db.models import Event, Attendee
from lib.db.database import session

def seed_database():
    """Seed the database with sample data."""

    # Clear existing data
    session.query(Event).delete()
    session.query(Attendee).delete()
    session.commit()

    # Create sample events
    event1 = Event(name="Tech Conference 2024", date="2024-10-25", location="Nairobi")
    event2 = Event(name="Python Workshop", date="2024-11-05", location="Online")
    event3 = Event(name="Data Science Summit", date="2025-02-15", location="Kisumu")
    session.add_all([event1, event2, event3])
    session.commit()

    # Create sample attendees
    attendee1 = Attendee(name="John Doe", email="john@example.com")
    attendee2 = Attendee(name="Jane Smith", email="jane@example.com")
    attendee3 = Attendee(name="Peter Jones", email="peter@example.com")
    session.add_all([attendee1, attendee2, attendee3])
    session.commit()

    # Register attendees for events
    event1.attendees.append(attendee1)
    event1.attendees.append(attendee2)
    event2.attendees.append(attendee2)
    session.commit()

    print("Database seeded successfully!")

if __name__ == '__main__':
    seed_database()