from lib.db.models import Event, Attendee
from lib.db.database import session
from lib.helpers import create_event_record, create_attendee_record, find_by_id, delete_record

def display_events():
    events = session.query(Event).all()
    if not events:
        print("No events found.")
    for event in events:
        print(f"ID: {event.id}, Name: {event.name}, Date: {event.date}, Location: {event.location}")
        print("  Attendees:")
        if not event.attendees:
            print("    No attendees registered.")
        for attendee in event.attendees:
            print(f"    - ID: {attendee.id}, Name: {attendee.name}")

def display_attendees():
    attendees = session.query(Attendee).all()
    if not attendees:
        print("No attendees found.")
    for attendee in attendees:
        print(f"ID: {attendee.id}, Name: {attendee.name}, Email: {attendee.email}")
        print("  Registered for events:")
        if not attendee.events:
            print("    No events registered.")
        for event in attendee.events:
            print(f"    - ID: {event.id}, Name: {event.name}")

def manage_events_menu():
    while True:
        print("\n--- Manage Events ---")
        print("1. Create a new event")
        print("2. View all events")
        print("3. Find event by ID")
        print("4. Add attendee to event")
        print("5. Delete an event")
        print("6. Back to main menu")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter event name: ")
            date = input("Enter event date (e.g., YYYY-MM-DD): ")
            location = input("Enter event location: ")
            print(create_event_record(name, date, location))
        elif choice == '2':
            display_events()
        elif choice == '3':
            event_id = input("Enter event ID: ")
            event = find_by_id(Event, event_id)
            if event:
                print(f"ID: {event.id}, Name: {event.name}, Date: {event.date}, Location: {event.location}")
            else:
                print("Event not found.")
        elif choice == '4':
            event_id = input("Enter event ID: ")
            attendee_id = input("Enter attendee ID to add: ")
            try:
                event = find_by_id(Event, int(event_id))
                attendee = find_by_id(Attendee, int(attendee_id))
                if event and attendee:
                    event.attendees.append(attendee)
                    session.commit()
                    print("Attendee added successfully!")
                else:
                    print("Event or Attendee not found.")
            except ValueError:
                print("Invalid ID. Please enter numbers.")
        elif choice == '5':
            event_id = input("Enter event ID to delete: ")
            print(delete_record(Event, event_id))
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

def manage_attendees_menu():
    while True:
        print("\n--- Manage Attendees ---")
        print("1. Create a new attendee")
        print("2. View all attendees")
        print("3. Find attendee by ID")
        print("4. Delete an attendee")
        print("5. Back to main menu")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter attendee name: ")
            email = input("Enter attendee email: ")
            print(create_attendee_record(name, email))
        elif choice == '2':
            display_attendees()
        elif choice == '3':
            attendee_id = input("Enter attendee ID: ")
            attendee = find_by_id(Attendee, attendee_id)
            if attendee:
                print(f"ID: {attendee.id}, Name: {attendee.name}, Email: {attendee.email}")
            else:
                print("Attendee not found.")
        elif choice == '4':
            attendee_id = input("Enter attendee ID to delete: ")
            print(delete_record(Attendee, attendee_id))
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def main_menu():
    while True:
        print("\n=== Event and Attendee Tracker ===")
        print("1. Manage Events")
        print("2. Manage Attendees")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            manage_events_menu()
        elif choice == '2':
            manage_attendees_menu()
        elif choice == '3':
            print("Exiting application. Goodbye!")
            session.close()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main_menu()