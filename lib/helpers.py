from lib.db.models import Event, Attendee
from lib.db.database import session
from sqlalchemy.exc import IntegrityError

def create_event_record(name, date, location):
    try:
        event = Event(name=name, date=date, location=location)
        session.add(event)
        session.commit()
        return "Event created successfully!"
    except Exception as e:
        session.rollback()
        return f"Error creating event: {e}"

def create_attendee_record(name, email):
    try:
        attendee = Attendee(name=name, email=email)
        session.add(attendee)
        session.commit()
        return "Attendee created successfully!"
    except IntegrityError:
        session.rollback()
        return "Error: An attendee with this email already exists."
    except Exception as e:
        session.rollback()
        return f"Error creating attendee: {e}"

def find_by_id(model, record_id):
    try:
        return session.query(model).filter_by(id=record_id).first()
    except:
        return None

def delete_record(model, record_id):
    record = find_by_id(model, record_id)
    if record:
        session.delete(record)
        session.commit()
        return "Record deleted successfully."
    else:
        return "Record not found."